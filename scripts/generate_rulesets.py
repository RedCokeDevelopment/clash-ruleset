#!/usr/bin/env python3
"""Generate aggregate Clash rule providers from the ruleset manifest."""

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "config" / "rulesets.yaml"


def parse_manifest() -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    current: str | None = None

    for raw_line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.endswith(":") and not line.startswith("-"):
            current = line[:-1]
            result[current] = []
        elif line.startswith("- ") and current:
            result[current].append(line[2:].strip())
        else:
            raise ValueError(f"Invalid manifest line: {raw_line}")

    return result


def rules_from_source(source: str) -> list[str]:
    path = ROOT / source
    if not path.is_file():
        raise FileNotFoundError(f"Manifest source does not exist: {source}")

    rules: list[str] = []
    in_payload = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line == "payload:":
            in_payload = True
            continue
        if in_payload and line.startswith("-"):
            rule = line[1:].strip()
            if rule and not rule.startswith("#"):
                rules.append(rule)
    return rules


def generate(name: str, entries: list[str], output_dir: Path) -> None:
    rules: list[str] = []
    for entry in entries:
        if entry.startswith("MATCH,"):
            rules.append(entry)
        else:
            rules.extend(rules_from_source(entry))

    unique_rules = list(dict.fromkeys(rules))
    output = "payload:\n" + "".join(f"  - {rule}\n" for rule in unique_rules)
    (output_dir / f"{name}.yaml").write_text(output, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for name, entries in parse_manifest().items():
        generate(name, entries, args.output_dir)


if __name__ == "__main__":
    main()
