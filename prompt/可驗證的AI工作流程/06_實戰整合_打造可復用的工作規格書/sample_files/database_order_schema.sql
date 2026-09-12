-- ========================================================
-- 電商訂單資料庫現有結構定義 (PostgreSQL)
-- 用於設計 GET /api/v1/orders 規格時對照欄位型態與隱私保護規範
-- ========================================================

-- 會員主表
CREATE TABLE users (
    user_id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    full_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL, -- 需遮罩！例如 0912****78
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 訂單主表
CREATE TABLE orders (
    order_id VARCHAR(32) PRIMARY KEY, -- 格式如 ORD-202609-8821
    user_id VARCHAR(36) NOT NULL REFERENCES users(user_id),
    status VARCHAR(20) NOT NULL, -- PENDING, PAID, SHIPPED, CANCELLED
    total_amount NUMERIC(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'TWD',
    credit_card_last4 VARCHAR(4), -- 信用卡末四碼，嚴禁回傳完整卡號！
    shipping_address TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 訂單明細表
CREATE TABLE order_items (
    item_id SERIAL PRIMARY KEY,
    order_id VARCHAR(32) NOT NULL REFERENCES orders(order_id),
    product_id VARCHAR(32) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    subtotal NUMERIC(10, 2) NOT NULL
);
