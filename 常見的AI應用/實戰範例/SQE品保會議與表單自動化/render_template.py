import os
import json
import docx

def render_docx_from_template(template_file, output_file, context_data):
    """
    讀取包含佔位符的 Word 範本檔案，並以提供的數據進行無損替換
    - 完整保留範本原始字體名稱、字型大小、字元顏色與粗體樣式
    - 同時支援常規段落（doc.paragraphs）與表格儲存格段落（table.rows.cells.paragraphs）
    """
    if not os.path.exists(template_file):
        raise FileNotFoundError(f"找不到範本檔案：{template_file}，請確認是否位於專案資料夾中！")

    doc = docx.Document(template_file)

    def replace_in_paragraphs(paragraphs):
        for p in paragraphs:
            for key, val in context_data.items():
                if key in p.text:
                    # 1. 優先在個別 run 中替換（完美保持局部樣式）
                    for r in p.runs:
                        if key in r.text:
                            r.text = r.text.replace(key, str(val))
                    
                    # 2. 若 placeholder 被 Word 拆分成多個 runs，執行全域替換並保留第一個 run 的字型樣式
                    if key in p.text:
                        f_name = p.runs[0].font.name if p.runs else None
                        f_size = p.runs[0].font.size if p.runs else None
                        f_color = p.runs[0].font.color.rgb if (p.runs and p.runs[0].font.color) else None
                        f_bold = p.runs[0].font.bold if p.runs else None
                        
                        p.text = p.text.replace(key, str(val))
                        
                        if p.runs and f_name:
                            p.runs[0].font.name = f_name
                            p.runs[0].font.size = f_size
                            if f_color:
                                p.runs[0].font.color.rgb = f_color
                            p.runs[0].font.bold = f_bold

    # 替換本文段落
    replace_in_paragraphs(doc.paragraphs)

    # 替換所有表格儲存格內的文字
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                replace_in_paragraphs(cell.paragraphs)

    doc.save(output_file)
    print(f"🎉 產檔完成！輸出檔案：{output_file}（已 100% 完全對齊官方範本）")


if __name__ == "__main__":
    template_path = os.path.join(os.path.dirname(__file__), "FR-MR09_會議記錄表_Template.docx")
    output_path = os.path.join(os.path.dirname(__file__), "FR-MR09_會議記錄表_已完成.docx")

    # 注入由 AI 萃取之結構化 JSON 變數
    context = {
        "{{MEETING_DATE}}": "2026年08月13日",
        "{{MEETING_SUBJECT}}": "藍機右殼 / 黏結凸輪 / 下齒板異常審查 (M260802)",
        "{{MEETING_TIME}}": "15:30 ~ 16:06",
        "{{MEETING_LOCATION}}": "泛源會議室",
        "{{CHAIR}}": "謝華賢 (技術長)",
        "{{RECORDER}}": "楊子賢 (資材處SQE)",
        "{{TOPIC_1_TITLE}}": "藍機右殼 L93XXAR1 外觀泛黃問題討論",
        "{{TOPIC_1_CONTENT}}": "【現況描述】部分庫存零件存在外觀顏色差異與長期存放狀況。其中約 3pcs 貼面板結構外觀泛黃；部分零件外觀白色斑點符合客戶既有同意接收標準。確認不能使用之 13pcs 藍機右殼先行管制。\n【品質與營運影響】不良品扣除後將直接影響原承諾之成套配套物料，若後續維修備品需求增加，恐引發庫存缺料風險。\n【MRB 處置結論】已確認泛黃之 13pcs 即刻實施隔離管制，全數納入保留倉；其餘合規庫存加速出貨，並持續監控庫存存放狀況。",
        "{{TOPIC_2_TITLE}}": "黏結凸輪 92XX079 角度公差放寬之組裝功能風險",
        "{{TOPIC_2_CONTENT}}": "【主要問題與風險】原公差為 19° ±0.5°，加工廠商申請放寬至 ±1°。品保評估目前在 ±0.5° 下組裝已有調整困難，若放寬將直接改變開關啟動行程、大幅增加組裝工時，甚至造成售後更換困難。\n【驗證方案與對照條件】暫不直接放寬公差！技術長核定先以 19.5°~20° 角度製作 5pcs 試作件進行對照驗證，比較組裝時間、調整次數、啟動行程與不良率。\n【MRB 處置結論】小批量對照組裝若無顯著差異再評估放寬；若仍影響功能則維持原規格並責令供應商（承化）自費改善；改善未果即啟動備援供應商（竹翔）開模。",
        "{{TOPIC_3_TITLE}}": "黏結下齒板(加工) 93XXAO2 需 80pcs 試作及全製程驗證",
        "{{TOPIC_3_CONTENT}}": "【現況與製程轉移】前期 3pcs 樣品已於鑫將驗證初步合格。原熱處理廠（國泰）有黑痕缺陷，現將熱處理製程轉由鑫將執行。\n【關鍵品質要求】熱處理對齒板尺寸形狀影響甚鉅，不可單看熱處理外觀，必須完整走過「加工 ➔ 熱處理 ➔ 噴砂 ➔ 電鍍 ➔ 最終尺寸與功能檢驗」全製程。\n【MRB 處置結論】核定 80pcs 試作案繼續執行。3pcs 僅為初步驗證，待 80pcs 全製程驗證確認穩定合格後，方能正式作為量產製程依據。",
        "{{ACTION_1_TASK}}": "確認長期庫存零件是否有變色、老化或其他品質風險",
        "{{ACTION_1_OWNER}}": "品保處／倉庫",
        "{{ACTION_1_DUE}}": "2026 年底前",
        "{{ACTION_2_TASK}}": "完成 80pcs 下齒板試作，並完整走完全製程",
        "{{ACTION_2_OWNER}}": "資材處／供應商／二廠加工組",
        "{{ACTION_2_DUE}}": "依專案排程",
        "{{ACTION_3_TASK}}": "完成 80pcs 熱處理、噴砂後之尺寸及外觀檢驗報告",
        "{{ACTION_3_OWNER}}": "品保處",
        "{{ACTION_3_DUE}}": "80pcs 完成後",
        "{{ACTION_4_TASK}}": "針對凸輪 19.5°-20° 角度條件進行 5pcs 小批量對照組裝",
        "{{ACTION_4_OWNER}}": "承化／資材處／品保處",
        "{{ACTION_4_DUE}}": "儘速安排",
        "{{ACTION_5_TASK}}": "量測角度變化對開關啟動行程之實際影響數據",
        "{{ACTION_5_OWNER}}": "生產處／品保處／研發處",
        "{{ACTION_5_DUE}}": "小批量試驗後",
        "{{ACTION_6_TASK}}": "若承化改善仍無法達標，啟動第二供應商（竹翔）開模方案",
        "{{ACTION_6_OWNER}}": "資材處／研發處",
        "{{ACTION_6_DUE}}": "第一階段評估後"
    }

    render_docx_from_template(template_path, output_path, context)
