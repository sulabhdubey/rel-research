"""Reconstruct Study 1's recorded table using only Python's standard library."""
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parent
TOKEN_FIELDS = ("total_tokens", "input_tokens", "cached_input_tokens",
                "output_tokens", "reasoning_output_tokens")
PHASES = ("total", "task", "feedback")
FILES = {"attempts.csv", "expected_summary.json", "source_provenance.json",
         "README.md", "reproduce.py"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def aggregate(rows, phase="total"):
    result = {key: sum(row[f"{phase}_{key}"] for row in rows)
              for key in TOKEN_FIELDS}
    result["uncached_input_plus_output"] = (
        result["input_tokens"] - result["cached_input_tokens"]
        + result["output_tokens"])
    return result


def main():
    manifest = {}
    for line in (ROOT / "MANIFEST.sha256").read_text("ascii").splitlines():
        digest, name = line.split("  ", 1)
        require(name in FILES and name not in manifest, "Unexpected manifest entry")
        manifest[name] = digest
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        require(actual == digest, f"Changed file: {name}")
    require(set(manifest) == FILES, "Incomplete manifest")

    with (ROOT / "attempts.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    require(len(rows) == 26 and len({r["cell"] for r in rows}) == 26,
            "Expected exactly 26 distinct attempts")
    numeric = ("repetition", "wave", "attempted", "identity_valid",
               "workflow_complete", "task_correct", "scored_total",
               "scored_pass", "scored_fail", "scored_unresolved")
    for row in rows:
        for key in numeric + tuple(f"{p}_{k}" for p in PHASES for k in TOKEN_FIELDS):
            row[key] = int(row[key])
            require(row[key] >= 0, f"Negative count: {row['cell']}/{key}")
        for key in ("attempted", "identity_valid", "workflow_complete", "task_correct"):
            require(row[key] in (0, 1), f"Invalid Boolean field: {key}")
        require(row["attempted"] == row["identity_valid"] == row["workflow_complete"] == 1,
                f"Unexpected missing/invalid attempt: {row['cell']}")
        require(row["scored_total"] == row["scored_pass"] + row["scored_fail"]
                + row["scored_unresolved"], f"Scored count mismatch: {row['cell']}")
        require(row["scored_total"] > 0 and row["scored_unresolved"] == 0,
                f"Unexpected unresolved score: {row['cell']}")
        require(row["task_correct"] == int(row["scored_fail"] == 0),
                f"Correctness mismatch: {row['cell']}")
        for phase in PHASES:
            usage = {k: row[f"{phase}_{k}"] for k in TOKEN_FIELDS}
            require(usage["total_tokens"] == usage["input_tokens"] + usage["output_tokens"],
                    f"Token arithmetic mismatch: {row['cell']}/{phase}")
            require(usage["cached_input_tokens"] <= usage["input_tokens"]
                    and usage["reasoning_output_tokens"] <= usage["output_tokens"],
                    f"Invalid token subset: {row['cell']}/{phase}")
        for key in TOKEN_FIELDS:
            require(row[f"total_{key}"] == row[f"task_{key}"] + row[f"feedback_{key}"],
                    f"Phase accounting mismatch: {row['cell']}/{key}")

    origins = [r for r in rows if r["stage"] == "origin"]
    later = [r for r in rows if r["stage"] == "followup"]
    require(len(origins) == 2 and {r["cell"] for r in origins} == {"O1", "O2"}
            and len(later) == 24, "Origin/follow-up inventory mismatch")
    require(all(r["arm"] == "R" and r["origin_id"] == r["cell"]
                and not r["pair_id"] and not r["transfer_task_id"]
                and r["repetition"] == 0 for r in origins), "Invalid origin role")
    acquisition = aggregate(origins)
    table = {}
    expected_blocks = {(o, t, p) for o in ("O1", "O2")
                       for t in ("schema_transfer_draft7", "schema_transfer_2020")
                       for p in (1, 2)}
    require({r["arm"] for r in later} == set("ABC"), "Invalid follow-up arm")
    for arm in "ABC":
        selected = [r for r in later if r["arm"] == arm]
        require(len(selected) == 8 and
                {(r["origin_id"], r["transfer_task_id"], r["repetition"])
                 for r in selected} == expected_blocks, f"Unmatched blocks: {arm}")
        for row in selected:
            task_label = "T1" if row["transfer_task_id"] == "schema_transfer_draft7" else "T2"
            pair = f"{row['origin_id']}-{task_label}-P{row['repetition']}"
            require(row["pair_id"] == pair and row["cell"] == f"{pair}-{arm}",
                    f"Role identity mismatch: {row['cell']}")
        later_usage = aggregate(selected)
        inclusive = {key: later_usage[key] + (acquisition[key] if arm != "A" else 0)
                     for key in later_usage}
        correct = sum(r["task_correct"] for r in selected)
        table[arm] = {"attempts": 8, "correct_tasks": correct,
                      "later_usage": later_usage, "inclusive_usage": inclusive,
                      "inclusive_tokens_per_correct_task": inclusive["total_tokens"] / correct}
    result = {"rows": len(rows), "origin_attempts": len(origins),
              "origin_correct_tasks": sum(r["task_correct"] for r in origins),
              "acquisition_usage": acquisition, "actual_campaign_usage": aggregate(rows),
              "actual_feedback_usage": aggregate(rows, "feedback"), "table": table}
    expected = json.loads((ROOT / "expected_summary.json").read_text("utf-8"))
    require(result == expected, "Exported aggregate differs from recorded summary")
    require([table[a]["correct_tasks"] for a in "ABC"] == [7, 8, 8]
            and [table[a]["inclusive_usage"]["total_tokens"] for a in "ABC"]
            == [1270553, 1475038, 1473718], "Published table mismatch")
    require(acquisition["total_tokens"] == 357417
            and result["actual_campaign_usage"]["total_tokens"] == 3861892,
            "Published campaign/acquisition mismatch")
    print(json.dumps({"verified_summary": result,
                      "scope": "Saved-record arithmetic only; no raw-event authentication or model rerun."}, indent=2))


if __name__ == "__main__":
    main()
