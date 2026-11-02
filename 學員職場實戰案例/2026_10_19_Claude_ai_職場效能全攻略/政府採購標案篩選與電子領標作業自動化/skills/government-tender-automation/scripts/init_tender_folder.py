#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
init_tender_folder.py
政府採購標案五合一標準目錄自動化建置腳本
"""

import argparse
import sys
from pathlib import Path

SUBDIRECTORIES = [
    "01_公告",
    "02_領標憑據及付款",
    "03_原始招標文件",
    "04_更正及補充",
    "05_內部評估",
]

def init_tender_folder(plan_id: int, category: str, name: str, base_dir: Path) -> Path:
    # 號段防呆檢核
    if category.lower() in ["target", "爭取"]:
        cat_folder = "標案爭取"
        if not (3001 <= plan_id <= 6000):
            print(f"[警告] 爭取標案建議編號區間為 3001～6000，目前輸入為: {plan_id}", file=sys.stderr)
    elif category.lower() in ["reference", "參考"]:
        cat_folder = "標案參考"
        if not (6001 <= plan_id <= 9999):
            print(f"[警告] 參考標案建議編號區間為 6001～9999，目前輸入為: {plan_id}", file=sys.stderr)
    else:
        cat_folder = "其他標案"

    # 建立目標資料夾名稱：[四碼編號]_[標案名稱]
    folder_name = f"{plan_id:04d}_{name.strip()}"
    project_path = base_dir / cat_folder / folder_name

    project_path.mkdir(parents=True, exist_ok=True)
    print(f"📁 建立標案主資料夾: {project_path}")

    # 建立五大子資料夾
    for sub in SUBDIRECTORIES:
        sub_path = project_path / sub
        sub_path.mkdir(exist_ok=True)
        print(f"  └── 📁 {sub}")

    # 建立 README 索引文字檔
    meta_file = project_path / "標案專案說明.txt"
    meta_content = f"""計畫編號：{plan_id:04d}
標案名稱：{name}
標案分類：{cat_folder}
建立時間：{Path().resolve()}
子目錄規範說明：
- 01_公告：收納採購網招標公告、初次公告 PDF 截圖
- 02_領標憑據及付款：收納電子領標憑據 (.tkn) 與付款刷卡收據（投標必備）
- 03_原始招標文件：初次下載之招標文件、投標須知、契約樣稿與需求說明書
- 04_更正及補充：機關後續發布之更正公告、截標展延、疑義釋疑回覆
- 05_內部評估：技術部內部評估表、競品分析、工項估算初稿
"""
    meta_file.write_text(meta_content, encoding="utf-8")
    print(f"  └── 📄 標案專案說明.txt 已生成")

    return project_path

def main():
    parser = argparse.ArgumentParser(description="建立政府採購標案五合一標準目錄結構")
    parser.add_argument("--id", type=int, required=True, help="四碼計畫編號 (例: 3043 或 6089)")
    parser.add_argument("--category", choices=["target", "reference", "爭取", "參考"], default="target", help="標案分類 (爭取/參考)")
    parser.add_argument("--name", type=str, required=True, help="標案名稱 (例: 水利署115年度水資源智慧監控委託技術服務案)")
    parser.add_argument("--outdir", type=str, default="./", help="輸出根目錄 (預設為當前目錄)")

    args = parser.parse_args()
    base_dir = Path(args.outdir).resolve()
    init_tender_folder(args.id, args.category, args.name, base_dir)
    print("\n✅ 五合一標準目錄建置完成！")

if __name__ == "__main__":
    main()

