#!/usr/bin/env python3
"""統計會議逐字稿的發言時間分配。

用法：
    python3 calculate_hours.py <逐字稿路徑>
    python3 calculate_hours.py <逐字稿路徑> --json

支援的時間戳記格式：
    [00:12:34] 說話者：內容
    [12:34]    說話者：內容
    09:15:30   說話者：內容
    (00:12:34) 說話者：內容

設計原則（供 skill 使用者參考）：
  - 找不到時間戳記時，明確回報並以退出碼 2 結束，
    而不是回傳看似合理的空結果。讓 skill 知道該跳過這一步。
  - 最後一位發言者的時長無法從下一個戳記推得，明確標示為「未知」，
    不做推估。這與 SKILL.md「不得補造」的原則一致。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# [00:12:34] / [12:34] / (00:12:34) / 行首的 09:15:30
TIMESTAMP_RE = re.compile(
    r"^\s*[\[\(]?(?P<ts>(?:\d{1,2}:)?\d{1,2}:\d{2})[\]\)]?\s*"
    r"(?P<speaker>[^：:]{1,20})?\s*[：:]?\s*(?P<text>.*)$"
)


def parse_timestamp(ts: str) -> int:
    """把 HH:MM:SS 或 MM:SS 轉成秒數。"""
    parts = [int(p) for p in ts.split(":")]
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h, m, s = 0, parts[0], parts[1]
    else:
        raise ValueError(f"無法解析的時間格式：{ts}")
    return h * 3600 + m * 60 + s


def fmt_duration(seconds: int) -> str:
    m, s = divmod(seconds, 60)
    return f"{m}分{s:02d}秒" if m else f"{s}秒"


def extract_segments(lines: list[str]) -> list[dict]:
    """抽出所有 (時間, 說話者) 片段。"""
    segments = []
    for raw in lines:
        m = TIMESTAMP_RE.match(raw)
        if not m:
            continue
        speaker = (m.group("speaker") or "").strip()
        if not speaker:
            continue
        try:
            at = parse_timestamp(m.group("ts"))
        except ValueError:
            continue
        segments.append({"at": at, "speaker": speaker, "text": m.group("text").strip()})
    return segments


def analyze(segments: list[dict]) -> dict:
    """計算每位發言者的時長佔比。

    最後一段的時長無法得知（沒有下一個戳記），標示為未知，不做推估。
    """
    by_speaker: dict[str, int] = defaultdict(int)
    turns: dict[str, int] = defaultdict(int)

    for i, seg in enumerate(segments):
        turns[seg["speaker"]] += 1
        if i + 1 < len(segments):
            duration = segments[i + 1]["at"] - seg["at"]
            if duration >= 0:  # 忽略時間倒退的異常戳記
                by_speaker[seg["speaker"]] += duration

    total = sum(by_speaker.values())
    rows = []
    for speaker, secs in sorted(by_speaker.items(), key=lambda kv: -kv[1]):
        rows.append({
            "speaker": speaker,
            "seconds": secs,
            "duration": fmt_duration(secs),
            "turns": turns[speaker],
            "share_pct": round(secs / total * 100, 1) if total else 0.0,
        })

    return {
        "total_seconds": total,
        "total_duration": fmt_duration(total),
        "segment_count": len(segments),
        "speakers": rows,
        "note": "最後一位發言者的時長無法從時間戳記推得，未計入總計。",
    }


def render_markdown(result: dict) -> str:
    out = ["## 議程時間分配", ""]
    out.append(f"**可計算的總時長**：{result['total_duration']}　"
               f"**發言片段數**：{result['segment_count']}")
    out.append("")
    out.append("| 發言者 | 時長 | 佔比 | 發言次數 |")
    out.append("| :--- | ---: | ---: | ---: |")
    for r in result["speakers"]:
        out.append(f"| {r['speaker']} | {r['duration']} | {r['share_pct']}% | {r['turns']} |")
    out.append("")
    out.append(f"> {result['note']}")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="統計會議逐字稿的發言時間分配")
    ap.add_argument("transcript", type=Path, help="逐字稿檔案路徑")
    ap.add_argument("--json", action="store_true", help="以 JSON 輸出")
    args = ap.parse_args()

    if not args.transcript.is_file():
        print(f"錯誤：找不到檔案 {args.transcript}", file=sys.stderr)
        return 1

    lines = args.transcript.read_text(encoding="utf-8").splitlines()
    segments = extract_segments(lines)

    if not segments:
        print("無時間資料：這份逐字稿沒有可解析的時間戳記。", file=sys.stderr)
        print("請在會議紀錄中註明「無時間資料」，不要推估。", file=sys.stderr)
        return 2

    if len(segments) < 3:
        print(f"時間資料不足：只找到 {len(segments)} 個時間戳記，"
              "不足以做有意義的統計。", file=sys.stderr)
        print("請在會議紀錄中註明「時間資料不完整」。", file=sys.stderr)
        return 2

    result = analyze(segments)
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json
          else render_markdown(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
