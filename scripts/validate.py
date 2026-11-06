#!/usr/bin/env python3
"""Validate portable skill metadata, local resources, Markdown links and CSV shape.

This is a static check, not a model evaluation or client compatibility test.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys instead of silently taking the last value."""


def unique_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode) -> dict:
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in mapping:
            raise ValueError(f"duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def frontmatter(path: Path) -> dict:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", path.read_text(encoding="utf-8"), re.S)
    if not match:
        raise ValueError("missing or malformed YAML frontmatter")
    data = yaml.load(match.group(1), Loader=UniqueKeyLoader)
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data


def prose_lines(text: str):
    """Ignore fenced examples so placeholder paths in shell commands aren't links."""
    marker = None
    length = 0
    for line in text.splitlines():
        fence = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence:
            run, suffix = fence.groups()
            if marker is None:
                marker, length = run[0], len(run)
            elif run[0] == marker and len(run) >= length and not suffix.strip():
                marker = None
            continue
        if marker is None:
            yield line


def validate(root: Path) -> tuple[list[str], dict[str, int]]:
    errors = []
    counts = {"skills": 0, "resource_refs": 0, "local_links": 0, "csv_files": 0}
    skills_root = root / "skills"
    if not skills_root.is_dir():
        errors.append("skills/: directory not found")

    for directory in sorted(skills_root.iterdir()) if skills_root.is_dir() else []:
        if not directory.is_dir():
            continue
        path = directory / "SKILL.md"
        counts["skills"] += 1
        try:
            data = frontmatter(path)
            name, description = data.get("name"), data.get("description")
            if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                raise ValueError("invalid skill name")
            if name != directory.name:
                raise ValueError("name must match directory")
            if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
                raise ValueError("description must contain 1–1024 characters")
            if "license" in data and data["license"] != "MIT":
                raise ValueError("check license against repository MIT license")
            for ref in re.findall(r"`((?:assets|references)/[^`]+)`", path.read_text(encoding="utf-8")):
                counts["resource_refs"] += 1
                if not (directory / ref).is_file():
                    errors.append(f"{path.relative_to(root)}: missing resource {ref}")
        except (OSError, ValueError, TypeError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")

    if counts["skills"] == 0:
        errors.append("skills/: no skills found")

    ignored = {".git", ".venv", "__pycache__"}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ignored.intersection(path.relative_to(root).parts):
            continue
        label = str(path.relative_to(root))
        if path.suffix == ".md":
            for line in prose_lines(path.read_text(encoding="utf-8")):
                line = re.sub(r"(`+).*?\1", "", line)
                for target in re.findall(r"!?\[[^\]]*\]\(([^)\s]+)\)", line):
                    target = target.strip("<>")
                    try:
                        parsed = urlsplit(target)
                    except ValueError:
                        errors.append(f"{label}: malformed link {target}")
                        continue
                    if parsed.scheme or parsed.netloc or not parsed.path:
                        continue
                    counts["local_links"] += 1
                    linked = path.parent / unquote(parsed.path)
                    if not linked.exists():
                        errors.append(f"{label}: broken local link {target}")
        elif path.suffix == ".csv":
            counts["csv_files"] += 1
            try:
                with path.open(encoding="utf-8-sig", newline="") as stream:
                    rows = list(csv.reader(stream, strict=True))
                if not rows or not rows[0] or any(not cell.strip() for cell in rows[0]):
                    raise ValueError("CSV needs a non-empty header")
                if len(set(rows[0])) != len(rows[0]):
                    raise ValueError("duplicate CSV column names")
                for number, row in enumerate(rows[1:], 2):
                    if len(row) != len(rows[0]):
                        raise ValueError(f"row {number}: expected {len(rows[0])} columns, found {len(row)}")
            except (OSError, ValueError, csv.Error) as exc:
                errors.append(f"{label}: {exc}")
    return errors, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, counts = validate(args.root.resolve())
    for error in errors:
        print(f"ERROR {error}")
    print(" | ".join(f"{key}={value}" for key, value in counts.items()))
    print("FAIL" if errors else "PASS (static checks only)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
