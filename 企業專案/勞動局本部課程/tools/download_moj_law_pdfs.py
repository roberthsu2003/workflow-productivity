#!/usr/bin/env python3
"""
自法務部全國法規資料庫下載「所有條文」PDF（教學／備課用）。
預設寫入 ../assets/（與本腳本相對路徑）。

注意：網站使用 ASP.NET 表單，需帶入 __VIEWSTATE 等欄位；若網站改版導致失敗，請改以瀏覽器手動下載。
若環境 SSL 驗證失敗，腳本會略過憑證驗證（僅限本機教學工具，請勿用於處理敏感資料之連線）。
"""

from __future__ import annotations

import re
import ssl
import sys
from pathlib import Path
from urllib import parse, request

# 與本課程範例對應之法規（DataId = 全國法規資料庫 pcode）
DEFAULT_LAWS: dict[str, str] = {
    "N0030001": "勞動基準法_全國法規資料庫",
    "N0030028": "最低工資法_全國法規資料庫",
    "N0030014": "性別平等工作法_全國法規資料庫",
    "N0060001": "職業安全衛生法_全國法規資料庫",
}

MAX_BYTES = 10 * 1024 * 1024  # 10 MB


def _opener():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return request.build_opener(request.HTTPSHandler(context=ctx))


def download_pdf(data_id: str) -> bytes:
    url = f"https://law.moj.gov.tw/LawClass/FilesType.aspx?DataId={data_id}&SLI=CALL"
    opener = _opener()
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (teaching; law-pdf-download)")]
    with opener.open(url, timeout=90) as r:
        html = r.read().decode("utf-8", errors="replace")
    m_vs = re.search(r'id="__VIEWSTATE" value="([^"]*)"', html)
    m_ev = re.search(r'id="__EVENTVALIDATION" value="([^"]*)"', html)
    m_vg = re.search(r'id="__VIEWSTATEGENERATOR" value="([^"]*)"', html)
    if not m_vs or not m_ev:
        raise RuntimeError(f"無法解析表單欄位：{data_id}")
    data = parse.urlencode(
        {
            "__VIEWSTATE": m_vs.group(1),
            "__VIEWSTATEGENERATOR": m_vg.group(1) if m_vg else "",
            "__EVENTVALIDATION": m_ev.group(1),
            "rdoFilesType": "PDF",
            "btnNoSDown": "下載",
        }
    ).encode("utf-8")
    req2 = request.Request(url, data=data, method="POST")
    with opener.open(req2, timeout=180) as r2:
        body = r2.read()
    if body[:4] != b"%PDF":
        raise RuntimeError(f"回應非 PDF：{data_id} 前 80 bytes：{body[:80]!r}")
    if len(body) > MAX_BYTES:
        raise RuntimeError(f"檔案超過 {MAX_BYTES} bytes：{len(body)}")
    return body


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    out_dir = root / "assets"
    out_dir.mkdir(parents=True, exist_ok=True)
    ok = 0
    for data_id, base_name in DEFAULT_LAWS.items():
        path = out_dir / f"{base_name}_{data_id}.pdf"
        try:
            body = download_pdf(data_id)
            path.write_bytes(body)
            print(f"OK {path.name} ({len(body):,} bytes)")
            ok += 1
        except Exception as e:
            print(f"FAIL {data_id}: {e}", file=sys.stderr)
    return 0 if ok == len(DEFAULT_LAWS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
