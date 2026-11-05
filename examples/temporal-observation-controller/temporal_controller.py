"""Ordinary lazy acquisition for explicitly scoped temporal reachability.

Only the caller's fetch callback obtains observations. This module contains no
network access, dataset reader, learned model, or hidden-truth evaluator.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import hashlib
import heapq
import json
from types import MappingProxyType
from typing import Callable, Iterable, Mapping


def _integer(value: object) -> bool:
    return type(value) is int


def _label(value: object, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"nonempty {name} required")


@dataclass(frozen=True)
class Event:
    """Undirected candidate contact; t is arrival/end time in integer units."""

    id: int
    t: int
    u: int
    v: int


@dataclass(frozen=True)
class Query:
    source: int
    target: int
    start: int
    deadline: int
    mode: str = "duration20"


def _events(events: Iterable[Event]) -> tuple[Event, ...]:
    rows = tuple(events)
    seen: set[int] = set()
    previous = None
    for event in rows:
        if not isinstance(event, Event) or not all(
            _integer(value) for value in (event.id, event.t, event.u, event.v)
        ):
            raise ValueError("integer Event fields required")
        if event.id < 0 or event.id in seen or event.u == event.v:
            raise ValueError("invalid or duplicate event identity")
        if previous is not None and (event.t, event.id) < previous:
            raise ValueError("events must be sorted by (t, id)")
        previous = (event.t, event.id)
        seen.add(event.id)
    return rows


def _query(query: Query) -> None:
    if not isinstance(query, Query) or not all(
        _integer(value)
        for value in (query.source, query.target, query.start, query.deadline)
    ):
        raise ValueError("integer Query fields required")
    if query.mode not in ("duration20", "instant"):
        raise ValueError("unsupported temporal semantics")
    if query.start > query.deadline:
        raise ValueError("reversed query window")


def identity(events: Iterable[Event]) -> str:
    """Hash the ordered public envelope, not its truth or completeness."""
    rows = _events(events)
    payload = json.dumps(
        [(event.id, event.t, event.u, event.v) for event in rows],
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


@dataclass(frozen=True)
class Scope:
    source_id: str
    version: str
    envelope_sha256: str

    def __post_init__(self) -> None:
        _label(self.source_id, "source identity")
        _label(self.version, "source version")
        if (
            not isinstance(self.envelope_sha256, str)
            or len(self.envelope_sha256) != 64
            or any(char not in "0123456789abcdef" for char in self.envelope_sha256)
        ):
            raise ValueError("lowercase SHA256 envelope identity required")

    @classmethod
    def for_events(cls, events: Iterable[Event], source_id: str, version: str) -> Scope:
        return cls(source_id, version, identity(events))


def _unique_json_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _invalid_json_constant(value: str) -> None:
    raise ValueError(f"invalid JSON constant: {value}")


class FactMemory:
    """Retain binary observations for exactly one source/version/envelope.

    The caller must change version whenever event validity can change. Facts are
    not query answers; different queries always recompute their bounds.
    """

    def __init__(self, events: Iterable[Event], source_id: str, version: str):
        rows = _events(events)
        self._scope = Scope.for_events(rows, source_id, version)
        self._valid_ids = frozenset(event.id for event in rows)
        self._facts: dict[int, int] = {}

    @property
    def scope(self) -> Scope:
        return self._scope

    @property
    def facts(self) -> Mapping[int, int]:
        return MappingProxyType(self._facts)

    def put(self, event_id: int, value: int) -> None:
        if not _integer(event_id) or event_id not in self._valid_ids:
            raise ValueError("unknown or invalid fact identity")
        if not _integer(value) or value not in (0, 1):
            raise ValueError("binary integer fact required")
        if event_id in self._facts and self._facts[event_id] != value:
            raise ValueError("conflicting fact")
        self._facts[event_id] = value

    def to_json(self) -> str:
        return json.dumps(
            {
                "schema": "temporal-facts-v1",
                "source_id": self.scope.source_id,
                "version": self.scope.version,
                "envelope_sha256": self.scope.envelope_sha256,
                "facts": sorted(self._facts.items()),
            },
            sort_keys=True,
            separators=(",", ":"),
        )

    @classmethod
    def from_json(
        cls, text: str, events: Iterable[Event], source_id: str, version: str
    ) -> FactMemory:
        """Strict small JSON checkpoint restore; no pickle or code execution."""
        if not isinstance(text, str):
            raise ValueError("JSON text required")
        memory = cls(events, source_id, version)
        packet = json.loads(
            text,
            object_pairs_hook=_unique_json_object,
            parse_constant=_invalid_json_constant,
        )
        keys = {"schema", "source_id", "version", "envelope_sha256", "facts"}
        if not isinstance(packet, dict) or set(packet) != keys:
            raise ValueError("invalid checkpoint fields")
        if packet["schema"] != "temporal-facts-v1":
            raise ValueError("unsupported checkpoint schema")
        if (
            packet["source_id"] != memory.scope.source_id
            or packet["version"] != memory.scope.version
            or packet["envelope_sha256"] != memory.scope.envelope_sha256
        ):
            raise ValueError("stale or wrong-scope checkpoint")
        if not isinstance(packet["facts"], list):
            raise ValueError("checkpoint facts must be a list")
        for row in packet["facts"]:
            if not isinstance(row, list) or len(row) != 2:
                raise ValueError("invalid checkpoint fact row")
            event_id, value = row
            if not _integer(event_id) or event_id in memory._facts:
                raise ValueError("invalid or duplicate checkpoint identity")
            memory.put(event_id, value)
        return memory


@dataclass(frozen=True)
class Decision:
    answer: bool | None
    witness: tuple[int, ...] | None
    requests: tuple[tuple[int, int], ...]
    reason: str
    path_checks: int
    edge_scans: int


def _relevant(events: tuple[Event, ...], query: Query) -> tuple[Event, ...]:
    lower = query.start + 20 if query.mode == "duration20" else query.start
    rows = tuple(event for event in events if lower <= event.t <= query.deadline)
    adjacency = defaultdict(set)
    for event in rows:
        adjacency[event.u].add(event.v)
        adjacency[event.v].add(event.u)
    seen = {query.source}
    queue = [query.source]
    while queue:
        node = queue.pop()
        for neighbour in adjacency[node] - seen:
            seen.add(neighbour)
            queue.append(neighbour)
    if query.target not in seen:
        return ()
    return tuple(event for event in rows if event.u in seen)


def _minimum_unknown_path(
    events: tuple[Event, ...], query: Query, allowed: set[int], known: set[int]
) -> tuple[tuple[int, ...] | None, int]:
    """Minimum unknown-event count, with waiting and immutable path witnesses."""
    if query.source == query.target:
        return (), 0
    available: dict[int, tuple[int, tuple[int, ...]]] = {}
    pending = [(query.start, 0, query.source, 0, ())]
    serial = 1
    work = 0
    answer = None
    answer_cost = float("inf")
    groups = defaultdict(list)
    for event in events:
        if event.id in allowed:
            groups[event.t].append(event)
    for time, rows in sorted(groups.items()):
        departure = time - 20 if query.mode == "duration20" else time
        while pending and pending[0][0] <= departure:
            _, _, node, cost, witness = heapq.heappop(pending)
            if cost < available.get(node, (float("inf"), ()))[0]:
                available[node] = (cost, witness)
        if query.mode == "duration20":
            for event in rows:
                weight = int(event.id not in known)
                for source, target in ((event.u, event.v), (event.v, event.u)):
                    work += 1
                    if source not in available:
                        continue
                    cost, witness = available[source]
                    new_cost = cost + weight
                    new_path = witness + (event.id,)
                    heapq.heappush(pending, (time, serial, target, new_cost, new_path))
                    serial += 1
                    if target == query.target and new_cost < answer_cost:
                        answer, answer_cost = new_path, new_cost
        else:
            adjacency = defaultdict(list)
            for event in rows:
                weight = int(event.id not in known)
                adjacency[event.u].append((event.v, event.id, weight))
                adjacency[event.v].append((event.u, event.id, weight))
            heap = [
                (cost, serial + index, node, witness)
                for index, (node, (cost, witness)) in enumerate(available.items())
                if node in adjacency
            ]
            serial += len(heap)
            heapq.heapify(heap)
            while heap:
                cost, _, node, witness = heapq.heappop(heap)
                if cost != available[node][0]:
                    continue
                for neighbour, event_id, weight in adjacency[node]:
                    work += 1
                    new_cost = cost + weight
                    if new_cost < available.get(neighbour, (float("inf"), ()))[0]:
                        new_path = witness + (event_id,)
                        available[neighbour] = (new_cost, new_path)
                        heapq.heappush(heap, (new_cost, serial, neighbour, new_path))
                        serial += 1
                        if neighbour == query.target and new_cost < answer_cost:
                            answer, answer_cost = new_path, new_cost
    return answer, work


def verify_witness(
    events: Iterable[Event], query: Query, witness: Iterable[int] | None,
    facts: Mapping[int, int],
) -> bool:
    """Check a positive certificate against acquired facts and temporal rules."""
    rows = _events(events)
    _query(query)
    if witness is None:
        return False
    by_id = {event.id: event for event in rows}
    node, at = query.source, query.start
    for event_id in witness:
        if not _integer(event_id) or event_id not in by_id:
            return False
        value = facts.get(event_id)
        if not _integer(value) or value != 1:
            return False
        event = by_id[event_id]
        departure = event.t - 20 if query.mode == "duration20" else event.t
        if departure < at or event.t > query.deadline or node not in (event.u, event.v):
            return False
        node = event.v if node == event.u else event.u
        at = event.t
    return node == query.target


def decide(
    events: Iterable[Event], query: Query, fetch: Callable[[int], int],
    memory: FactMemory, *, source_id: str, version: str, complete: bool,
    budget: int | None = None, policy: str = "lazy",
) -> Decision:
    """Acquire facts until lower/upper bounds decide or the budget runs out.

    lazy: choose a feasible path with the fewest unknown events; fetch its first
    unknown event. eager: fetch all relevant unknown events (up to budget), after
    honoring initially decisive bounds. Budgets count callback acquisitions.
    """
    rows = _events(events)
    _query(query)
    expected_scope = Scope.for_events(rows, source_id, version)
    if not isinstance(memory, FactMemory) or memory.scope != expected_scope:
        raise ValueError("stale or wrong-scope live memory")
    if type(complete) is not bool:
        raise ValueError("complete must be an explicit boolean")
    if budget is not None and (not _integer(budget) or budget < 0):
        raise ValueError("budget must be a nonnegative integer")
    if policy not in ("lazy", "eager"):
        raise ValueError("unknown policy")
    if not callable(fetch):
        raise ValueError("fetch callback required")
    rows = _relevant(rows, query)
    limit = len(rows) if budget is None else budget
    requests: list[tuple[int, int]] = []
    checks = work = 0

    def bounds():
        nonlocal checks, work
        known = {event_id for event_id, value in memory.facts.items() if value == 1}
        lower, scanned = _minimum_unknown_path(rows, query, known, known)
        checks += 1
        work += scanned
        if lower is not None:
            if not verify_witness(rows, query, lower, memory.facts):
                raise AssertionError("invalid produced witness")
            return lower, None
        allowed = {event.id for event in rows if memory.facts.get(event.id) != 0}
        upper, scanned = _minimum_unknown_path(rows, query, allowed, known)
        checks += 1
        work += scanned
        return None, upper

    def result(answer, witness, reason):
        return Decision(answer, witness, tuple(requests), reason, checks, work)

    def purchase(event_id):
        value = fetch(event_id)
        memory.put(event_id, value)
        requests.append((event_id, value))

    lower, upper = bounds()
    if lower is not None:
        return result(True, lower, "positive_witness")
    if upper is None:
        return result(False if complete else None, None,
                      "complete_upper_refutation" if complete else "incomplete_envelope")
    if policy == "eager":
        for event in rows:
            if event.id not in memory.facts and len(requests) < limit:
                purchase(event.id)
        lower, upper = bounds()
        if lower is not None:
            return result(True, lower, "positive_witness")
        if upper is None:
            return result(False if complete else None, None,
                          "complete_upper_refutation" if complete else "incomplete_envelope")
        return result(None, None, "budget_exhausted")
    while len(requests) < limit:
        unknown = [event_id for event_id in upper if event_id not in memory.facts]
        if not unknown:
            raise AssertionError("bounds disagree without an unknown fact")
        purchase(unknown[0])
        lower, upper = bounds()
        if lower is not None:
            return result(True, lower, "positive_witness")
        if upper is None:
            return result(False if complete else None, None,
                          "complete_upper_refutation" if complete else "incomplete_envelope")
    return result(None, None, "budget_exhausted")
