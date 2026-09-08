import test from "node:test";
import assert from "node:assert/strict";
import { calculateShipping } from "../src/shipping.js";

test("第一公斤使用區域基本費", () => {
  assert.equal(calculateShipping(1, "North"), 8000);
});

test("超過第一公斤以每公斤 1500 分進位", () => {
  assert.equal(calculateShipping(2.2, "Central"), 12000);
});

test("拒絕未知區域與無效重量", () => {
  assert.throws(() => calculateShipping(1, "Moon"), RangeError);
  assert.throws(() => calculateShipping(0, "North"), TypeError);
});
