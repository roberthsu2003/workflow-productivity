# -*- coding: utf-8 -*-
"""申報檔共用工具：統編／身分證檢查、全形轉換、民國日期。"""
import datetime, re

_LETTER = dict(zip("ABCDEFGHJKLMNPQRSTUVXYWZIO", [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]))

def check_company_id(n):
    """營利事業統一編號邏輯檢查（8碼）。"""
    if not re.fullmatch(r"\d{8}", n or ""): return False
    t = 0
    for d, w in zip(map(int, n), [1, 2, 1, 2, 1, 2, 4, 1]):
        p = d * w; t += p // 10 + p % 10
    return t % 10 == 0 or (n[6] == "7" and (t + 1) % 10 == 0)

def check_person_id(n):
    """國民身分證統一編號形式檢查（證號別0）。"""
    if not re.fullmatch(r"[A-Z][12]\d{8}", n or ""): return False
    c = _LETTER[n[0]]
    total = c // 10 + (c % 10) * 9 + sum(int(d) * w for d, w in zip(n[1:9], [8, 7, 6, 5, 4, 3, 2, 1])) + int(n[9])
    return total % 10 == 0

def to_fullwidth(s):
    out = []
    for ch in s:
        o = ord(ch)
        if ch == " ": out.append("\u3000")
        elif 0x21 <= o <= 0x7E: out.append(chr(o + 0xFEE0))
        else: out.append(ch)
    return "".join(out)

def pad_fullwidth(s, n):
    s = to_fullwidth(s)[:n]
    return s + "\u3000" * (n - len(s))

def roc_date(d):           # yyymmdd
    return f"{d.year - 1911:03d}{d.month:02d}{d.day:02d}"

def roc_ym(d):             # yyymm
    return f"{d.year - 1911:03d}{d.month:02d}"

def to_date(v):
    if isinstance(v, datetime.datetime): return v.date()
    if isinstance(v, datetime.date): return v
    if isinstance(v, str) and v.strip():
        for f in ("%Y-%m-%d", "%Y/%m/%d"):
            try: return datetime.datetime.strptime(v.strip(), f).date()
            except ValueError: pass
    return None

def month_end(y, m):
    nxt = datetime.date(y + (m == 12), m % 12 + 1, 1)
    return nxt - datetime.timedelta(days=1)

PLACEHOLDERS = {"vat_tax_no": "000000000", "wh_tax_no": "000000000", "tax_office": "A00", "nhi_unit": "000000000", "house_tax_no": "A00000000000"}

def config_problems(cfg, keys):
    """回傳設定缺漏或仍是範例值的項目。"""
    bad = []
    for k in keys:
        v = cfg.get(k, "")
        if not v or v == PLACEHOLDERS.get(k) or "範例" in v or v.startswith("example@"): bad.append(k)
    return bad
