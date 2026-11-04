"""Read-only checks for this skill's portable files, links, and two manifests."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit


CORE_DIRECTORIES = {"assets", "references", "scripts"}
EXCLUDED_DIRECTORIES = {".git", "__pycache__"}
PRIVATE_PATH = re.compile(
    r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]"
    r"|/(?:Users|home)/[^/\s]+"
    r"|\\\\[A-Za-z0-9_.-]+[\\/][A-Za-z0-9_.-]+"
    r"|\bfile:[/]{2}"
)
FENCE = re.compile(r"^ {0,3}(\x60{3,}|~{3,})")
INLINE_LINK = re.compile(
    r"!?\[(?:\\.|[^\]\\])*\]\(\s*"
    r"(?P<target><[^>\n]+>|(?:\\.|[^\s)\\])+)"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
REFERENCE_LINK = re.compile(
    r"^ {0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", re.MULTILINE
)


def issue(errors, code, path, detail):
    errors.append({"code": code, "path": path, "detail": detail})


def inventory(root, errors):
    """Do not follow filesystem links into material outside the package."""
    files = {}
    pending = [root]
    while pending:
        folder = pending.pop()
        for path in sorted(folder.iterdir()):
            relative = path.relative_to(root).as_posix()
            if path.name in EXCLUDED_DIRECTORIES:
                continue
            if path.is_symlink() or path.resolve() != path.absolute():
                issue(errors, "symlink", relative, "Package links are unsupported.")
                continue
            if path.is_dir():
                pending.append(path)
            elif path.is_file() and path.suffix not in (".pyc", ".pyo"):
                files[relative] = path.read_bytes()
    return files


def manifest_path(raw):
    return (
        bool(raw) and not any(character in raw for character in ("\\", ":", "\x00"))
        and not PurePosixPath(raw).is_absolute()
        and all(part not in ("", ".", "..") for part in raw.split("/"))
    )


def check_manifest(name, expected, files, errors):
    if name not in files:
        issue(errors, "manifest_unavailable", name, "Required manifest is missing.")
        return
    try:
        text = files[name].decode("utf-8-sig")
    except UnicodeError:
        issue(errors, "manifest_syntax", name, "Manifest must be UTF-8 text.")
        return
    entries = {}
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            issue(errors, "manifest_syntax", name, "Invalid row " + str(number))
            continue
        digest, relative = match.groups()
        if not manifest_path(relative):
            issue(errors, "manifest_path", name, "Unsafe path at row " + str(number))
            continue
        if relative in entries:
            issue(errors, "manifest_duplicate", name, "Duplicate entry: " + relative)
        entries[relative] = digest
    for relative in sorted(expected - entries.keys()):
        issue(errors, "manifest_missing", name, "Unlisted file: " + relative)
    for relative in sorted(entries.keys() - expected):
        issue(errors, "manifest_extra", name, "Out-of-scope or absent file: " + relative)
    for relative in sorted(expected & entries.keys()):
        if hashlib.sha256(files[relative]).hexdigest() != entries[relative]:
            issue(errors, "manifest_digest", name, "Changed bytes: " + relative)


def check_frontmatter(files, errors):
    try:
        lines = files["SKILL.md"].decode("utf-8-sig").splitlines()
        closing = lines.index("---", 1) if lines and lines[0] == "---" else -1
    except (KeyError, UnicodeError, ValueError):
        closing = -1
    if closing < 0:
        issue(errors, "frontmatter", "SKILL.md", "Missing UTF-8 frontmatter delimiters.")
        return
    values = {}
    for line in lines[1:closing]:
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9_-]*):\s*(.*)", line)
        if not match:
            continue
        key, value = match.groups()
        if key in values:
            issue(errors, "frontmatter", "SKILL.md", "Duplicate field: " + key)
        values[key] = value.strip().strip("\"'")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", values.get("name", "")):
        issue(errors, "frontmatter", "SKILL.md", "Name must use lowercase words and hyphens.")
    elif len(values["name"]) >= 64:
        issue(errors, "frontmatter", "SKILL.md", "Name must be shorter than 64 characters.")
    description = values.get("description", "")
    if (not description or description in ("|", ">", "null", "~")
            or description.startswith("#")):
        issue(errors, "frontmatter", "SKILL.md", "A nonempty scalar description is required.")


def prose_only(markdown):
    """Ignore fenced examples and inline code, which do not create file links."""
    kept = []
    fence = None
    for line in markdown.splitlines():
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            kept.append(line)
    return re.sub(r"(\x60+)(.+?)\1", "", "\n".join(kept), flags=re.DOTALL)


def check_links(root, relative, markdown, errors):
    prose = prose_only(markdown)
    targets = [match.group("target") for match in INLINE_LINK.finditer(prose)]
    targets.extend(match.group(1) for match in REFERENCE_LINK.finditer(prose))
    checked = 0
    for raw in targets:
        target = raw[1:-1] if raw.startswith("<") else raw
        try:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            checked += 1
            path = unquote(parsed.path)
            resolved = (root / relative).parent.joinpath(path).resolve()
            if ("\\" in path or PurePosixPath(path).is_absolute()
                    or not resolved.is_relative_to(root) or not resolved.exists()):
                issue(errors, "relative_link", relative,
                      "Missing, absolute, or escaping local destination: " + target)
        except (OSError, ValueError):
            issue(errors, "relative_link", relative, "Invalid local link destination.")
    return checked


def validate(root, core_only=False):
    errors = []
    files = inventory(root, errors)
    core = {path for path in files if path == "SKILL.md"
            or path.split("/")[0] in CORE_DIRECTORIES}
    package = set(files) - {"PACKAGE.sha256"}
    check_frontmatter(files, errors)
    check_manifest("MANIFEST.sha256", core, files, errors)
    if not core_only:
        check_manifest("PACKAGE.sha256", package, files, errors)
    links = 0
    for relative, raw in sorted(files.items()):
        if core_only and relative not in core | {"MANIFEST.sha256"}:
            continue
        try:
            content = raw.decode("utf-8-sig")
        except UnicodeError:
            continue
        for number, line in enumerate(content.splitlines(), 1):
            if PRIVATE_PATH.search(line):
                issue(errors, "private_path", relative,
                      "Absolute local path pattern at line " + str(number))
        if relative.endswith(".md"):
            links += check_links(root, relative, content, errors)
    return {
        "valid": not errors,
        "scope": "core-only" if core_only else "full-package",
        "errors": errors,
        "core_files": len(core),
        "package_files": None if core_only else len(package),
        "relative_links_checked": links,
        "limit": "Structural checks and UTF-8 local-path patterns only; no full YAML/"
                 "Markdown parser, secret audit, author authentication, or efficacy claim.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1])
    parser.add_argument("--core-only", action="store_true",
                        help="Validate installed core files and MANIFEST.sha256 without PACKAGE.sha256.")
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        if not root.is_dir():
            raise ValueError("Package root is not a directory.")
        result = validate(root, core_only=args.core_only)
    except (OSError, ValueError):
        print(json.dumps({"valid": False, "errors": [{
            "code": "package_unavailable", "path": ".",
            "detail": "Package root or files could not be read.",
        }]}))
        return 2
    print(json.dumps(result, ensure_ascii=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
