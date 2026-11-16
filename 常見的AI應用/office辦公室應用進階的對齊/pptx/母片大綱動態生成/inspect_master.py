"""步驟 1：掃描公司 .pptx 母片的所有版面配置 (Slide Layouts) 與原生佔位符 (Placeholders)。"""

import json
import sys
from pathlib import Path
from pptx import Presentation


def inspect_master(pptx_path: Path) -> list[dict]:
    """讀取 .pptx 並回傳所有 Slide Layout 與其佔位符結構清單。"""
    prs = Presentation(str(pptx_path))
    catalog = []
    for idx, layout in enumerate(prs.slide_layouts):
        placeholders = []
        for ph in layout.placeholders:
            placeholders.append({
                "idx": ph.placeholder_format.idx,
                "name": ph.name,
                "type": str(ph.placeholder_format.type).split(".")[-1].split(" ")[0],
            })
        catalog.append({
            "layout_index": idx,
            "layout_name": layout.name,
            "placeholders": placeholders,
        })
    return catalog


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "企業母片範本.pptx"
    result = inspect_master(target)
    print(json.dumps(result, ensure_ascii=False, indent=2))
