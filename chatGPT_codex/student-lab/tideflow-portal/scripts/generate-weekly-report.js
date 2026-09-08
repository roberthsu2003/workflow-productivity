import { mkdir, readFile, writeFile } from "node:fs/promises";

const read = (name) => readFile(new URL(`../data/${name}`, import.meta.url), "utf8");
const [delivery, issues, prs, commits] = await Promise.all([
  read("delivery_2026-W36.csv"), read("issues.csv"), read("pull_requests.csv"), read("commits.md")
]);
const missing = delivery.split("\n").filter((line) => line.includes(",,,,")).length;
const stalePr = prs.split("\n").filter((line) => line.includes("2026-08-")).length;
const failedPr = prs.split("\n").filter((line) => line.includes(",failed,")).length;
const openIssues = issues.split("\n").filter((line) => line.includes(",open,")).length;
const completed = commits.split("\n").filter((line) => line.startsWith("- `")).length;
const report = `# 2026-W36 營運週報\n\n## 已完成\n\n- ${completed} 筆模擬 commit，詳見 \`data/commits.md\`。\n\n## 風險\n\n- ${failedPr} 個 PR 測試失敗。\n- ${stalePr} 個 PR 超過 7 天未更新。\n- ${missing} 筆配送資料缺漏；未以 0 或推估值補齊。\n- ${openIssues} 個 Issue 尚未關閉。\n\n## 本週建議\n\n1. 先處理失敗的結帳測試。\n2. 追蹤東區準時率低於 95% 的原因。\n3. 向 WMS 負責人確認缺漏資料。\n`;
const directory = new URL("../reports/", import.meta.url);
await mkdir(directory, { recursive: true });
await writeFile(new URL("2026-W36_週報.md", directory), report, { flag: "wx" });
console.log("created reports/2026-W36_週報.md");
