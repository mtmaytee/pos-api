-- สร้างตาราง Category
CREATE TABLE IF NOT EXISTS m_category (
    category_id VARCHAR(10) PRIMARY KEY,
    category_name_th VARCHAR(100) NOT NULL
);

-- สร้างตาราง Product Type
CREATE TABLE IF NOT EXISTS m_product_type (
    type_id VARCHAR(10) PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL
);

-- สร้างตาราง Connection
CREATE TABLE IF NOT EXISTS m_connection (
    connection_id SERIAL PRIMARY KEY,
    contact_name VARCHAR(150) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    province_name VARCHAR(100) NOT NULL,
    location_name VARCHAR(200),
    booking_conditions TEXT
);

-- สร้างตาราง Product
CREATE TABLE IF NOT EXISTS m_product (
    product_id SERIAL PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    category_id VARCHAR(10) REFERENCES m_category(category_id),
    type_id VARCHAR(10) REFERENCES m_product_type(type_id),
    cost_price DECIMAL(10, 2) DEFAULT 0.0,
    selling_price DECIMAL(10, 2) DEFAULT 0.0,
    stock_qty INTEGER DEFAULT 0
);

-- สร้างตาราง Event Schedule
CREATE TABLE IF NOT EXISTS t_event_schedule (
    event_id SERIAL PRIMARY KEY,
    event_title VARCHAR(200) NOT NULL,
    connection_id INTEGER NOT NULL REFERENCES m_connection(connection_id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    booking_status VARCHAR(20) DEFAULT 'Pending',
    total_booth_fee DECIMAL(10, 2) DEFAULT 0.0
);

-- สร้าง Index 
CREATE INDEX IF NOT EXISTS idx_m_connection_province ON m_connection(province_name);
CREATE INDEX IF NOT EXISTS idx_m_product_sku ON m_product(sku);
CREATE INDEX IF NOT EXISTS idx_m_product_category ON m_product(category_id);
CREATE INDEX IF NOT EXISTS idx_m_product_type ON m_product(type_id);
CREATE INDEX IF NOT EXISTS idx_t_event_schedule_connection ON t_event_schedule(connection_id);