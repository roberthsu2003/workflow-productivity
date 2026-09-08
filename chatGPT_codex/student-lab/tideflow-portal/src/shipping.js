export function calculateShipping(weightKg, region) {
  if (!Number.isFinite(weightKg) || weightKg <= 0) {
    throw new TypeError("weightKg must be a positive number");
  }
  const base = { North: 8000, Central: 9000, South: 10000, East: 12000 }[region];
  if (base === undefined) throw new RangeError(`unsupported region: ${region}`);
  return base + Math.max(0, Math.ceil(weightKg - 1)) * 1500;
}
