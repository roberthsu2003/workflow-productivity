#!/usr/bin/env python3
"""Validate the structure and local links of the ChatGPT productivity handbook."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_TOP_LEVEL = (
    "00_Free_Desktop_vs_Web",
    "01_Settings",
    "02_Personalization",
    "03_Canvas",
    "04_Chats",
    "05_Advanced_Data_Analysis",
    "06_Work",
    "07_Projects",
    "08_Connectors",
    "09_Plugins",
    "10_Skills",
    "11_Local_MCP",
    "12_Custom_GPTs",
    "13_Web_and_Deep_Research",
    "14_Images",
    "15_Voice_Vision",
    "student-lab",
    "Troubleshooting",
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

    markdown_files = sorted(ROOT.rglob("*.md"))
    for md in markdown_files:
        content = md.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(content):
            target = local_target(md, match.group(1))
            if target and not target.exists():
                errors.append(f"{md.relative_to(ROOT)}: 連結失效 -> {match.group(1)}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("❌ 架構驗證失敗：")
        for error in errors:
            print(f"  - {error}")
        return 1

    md_count = len(list(ROOT.rglob("*.md")))
    file_count = len([p for p in ROOT.rglob("*") if p.is_file()])
    print("✅ ChatGPT 講義架構驗證通過！")
    print(f"  - 必備目錄數：{len(REQUIRED_TOP_LEVEL)}")
    print(f"  - Markdown 文件數：{md_count}")
    print(f"  - 全部檔案數：{file_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
