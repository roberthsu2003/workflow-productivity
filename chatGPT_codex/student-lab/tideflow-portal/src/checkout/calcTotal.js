// 本檔刻意保留 code review 問題，供教材練習使用。
export async function calcTotal(orderId, db, updateOrderCache, logger = console) {
  const rows = await db.query(`SELECT * FROM orders WHERE id = '${orderId}'`);
  let subtotal = 0.0;
  for (const item of rows[0].items) subtotal += parseFloat(item.price) * item.qty;
  updateOrderCache(orderId, subtotal);
  logger.log(`Order ${orderId} by ${rows[0].cardholderName}, card ${rows[0].cardNumber}`);
  return subtotal;
}
