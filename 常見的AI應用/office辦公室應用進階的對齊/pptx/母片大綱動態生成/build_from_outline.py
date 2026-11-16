"""步驟 3：根據公司母片 (.pptx) 與 AI 規劃的分頁規格 (slide_plan.json) 動態生成簡報並防溢出。"""

import json
import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Pt


def clear_existing_slides(prs: Presentation) -> None:
    """若公司母片檔案中原本帶有範例頁，清空主投影片區，僅保留母片與版型。"""
    for sld_id in list(prs.slides._sldIdLst):
        prs.part.drop_rel(sld_id.rId)
        prs.slides._sldIdLst.remove(sld_id)


def fill_placeholder(ph, content, max_chars: int = 160, shrink_pt: float = 13.0) -> None:
    """填入文字或條列清單至母片佔位符，開啟 word_wrap 並在過長時自動縮字防溢出。"""
    tf = ph.text_frame
    tf.word_wrap = True
    tf.clear()

    items = content if isinstance(content, list) else [str(content)]
    total_chars = sum(len(item["text"] if isinstance(item, dict) else str(item)) for item in items)

    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if isinstance(item, dict):
            p.text = item.get("text", "")
            p.level = int(item.get("level", 0))
        else:
            p.text = str(item)
            p.level = 0

        if total_chars > max_chars:
            for run in p.runs:
                run.font.size = Pt(shrink_pt)


def remove_unused_placeholders(slide, used_indices: set[int]) -> None:
    """移除未填入內容的佔位符，避免編輯時出現「按一下以新增文字」空框。"""
    for ph in list(slide.placeholders):
        if ph.placeholder_format.idx not in used_indices:
            sp = ph._element
            sp.getparent().remove(sp)


def build_presentation(master_path: Path, plan_path: Path, output_path: Path) -> None:
    """依 slide_plan.json 動態新增投影片並套用公司母片版型。"""
    prs = Presentation(str(master_path))
    clear_existing_slides(prs)

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    for slide_spec in plan["slides"]:
        layout = prs.slide_layouts[slide_spec["layout_index"]]
        slide = prs.slides.add_slide(layout)

        used = set()
        for idx_str, content in slide_spec["placeholders"].items():
            ph_idx = int(idx_str)
            if ph_idx in {p.placeholder_format.idx for p in slide.placeholders}:
                fill_placeholder(slide.placeholders[ph_idx], content)
                used.add(ph_idx)

        remove_unused_placeholders(slide, used)

    prs.save(str(output_path))
    print(f"已產出簡報：{output_path}（共 {len(prs.slides)} 頁）")


if __name__ == "__main__":
    base = Path(__file__).parent
    master = Path(sys.argv[1]) if len(sys.argv) > 1 else base / "企業母片範本.pptx"
    plan = Path(sys.argv[2]) if len(sys.argv) > 2 else base / "slide_plan.json"
    out = Path(sys.argv[3]) if len(sys.argv) > 3 else base / "簡報_母片動態生成示範.pptx"
    build_presentation(master, plan, out)
