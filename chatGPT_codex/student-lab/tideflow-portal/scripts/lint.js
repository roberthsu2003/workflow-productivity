import { readFile } from "node:fs/promises";

const targets = ["src/shipping.js", "src/server.js"];
let failed = false;
for (const target of targets) {
  const source = await readFile(new URL(`../${target}`, import.meta.url), "utf8");
  if (source.includes("\t")) {
    console.error(`${target}: 不可使用 tab`);
    failed = true;
  }
}
if (failed) process.exitCode = 1;
else console.log(`PASS: ${targets.length} files`);
