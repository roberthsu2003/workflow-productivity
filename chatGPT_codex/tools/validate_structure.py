#!/usr/bin/env python3
"""Validate the structure and local links of the chatGPT_codex handbook."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_TOP_LEVEL = (
    "Quickstart",
    "Settings",
    "Tasks",
    "Projects",
    "Agent_Configuration",
    "Skills",
    "Connectors",
    "Plugins",
    "MCP",
    "Browser",
    "Visualizations",
    "Workspaces",
    "Automations",
    "Remote",
    "student-lab",
    "Answer_Key",
    "Troubleshooting",
    "Offline_Mode",
    "tools",
)
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def local_target(markdown_file: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith("#"):
        return None
    if re.match(r"^[a-z][a-z0-9+.-]*:", target, flags=re.IGNORECASE):
        return None
    path_part = unquote(target.split("#", 1)[0])
    return (markdown_file.parent / path_part).resolve()


def validate() -> list[str]:
    errors: list[str] = []

    for name in REQUIRED_TOP_LEVEL:
        directory = ROOT / name
        if not directory.is_dir():
            errors.append(f"缺少必備目錄：{name}/")
        elif name != "tools" and not (directory / "README.md").is_file():
            errors.append(f"缺少主題入口：{name}/README.md")

    for directory in sorted(path for path in ROOT.rglob("*") if path.is_dir()):
        if not any(directory.iterdir()):
            errors.append(f"空資料夾：{directory.relative_to(ROOT)}/")

    for examples in sorted(ROOT.rglob("Examples")):
        for item in sorted(path for path in examples.iterdir() if path.is_dir()):
            has_entry = (item / "README.md").is_file() or any(item.glob("*.md"))
            if not has_entry:
                errors.append(f"案例沒有 Markdown 入口：{item.relative_to(ROOT)}/")

    for skill_file in sorted(ROOT.rglob("SKILL.md")):
        if skill_file.stat().st_size == 0:
            errors.append(f"空白 skill：{skill_file.relative_to(ROOT)}")

    lab = ROOT / "student-lab" / "tideflow-portal"
    for relative in (
        "package.json", "AGENTS.md", "src/server.js", "src/shipping.js",
        "src/checkout/calcTotal.js", "test/shipping.test.js",
        "scripts/bootstrap.sh", "scripts/generate-weekly-report.js",
        "data/delivery_2026-W36.csv", "data/issues.csv",
        "data/pull_requests.csv", "data/commits.md",
        "data/public_equity_source_snapshot.md",
    ):
        if not (lab / relative).is_file():
            errors.append(f"學生練習專案缺少：student-lab/tideflow-portal/{relative}")

    for markdown_file in sorted(ROOT.rglob("*.md")):
        content = markdown_file.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(content):
            target = local_target(markdown_file, match.group(1))
            if target is not None and not target.exists():
                line = content.count("\n", 0, match.start()) + 1
                relative_file = markdown_file.relative_to(ROOT)
                errors.append(f"失效連結：{relative_file}:{line} -> {match.group(1)}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print(f"FAIL: 發現 {len(errors)} 個架構問題")
        for error in errors:
            print(f"- {error}")
        return 1

    markdown_count = sum(1 for _ in ROOT.rglob("*.md"))
    file_count = sum(1 for path in ROOT.rglob("*") if path.is_file())
    print(f"PASS: {len(REQUIRED_TOP_LEVEL)} 個必備目錄、{markdown_count} 份 Markdown、{file_count} 個檔案皆通過檢查")
    return 0


if __name__ == "__main__":
    sys.exit(main())
