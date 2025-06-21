CREATE TABLE IF NOT EXISTS staging_customers (
    customer_id VARCHAR(50),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    registration_date TIMESTAMP,
    extraction_source VARCHAR(50),
    extraction_date TIMESTAMP,
    PRIMARY KEY (customer_id, extraction_date)
);

CREATE TABLE IF NOT EXISTS staging_users (
    id INTEGER,
    name VARCHAR(100),
    username VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(50),
    website VARCHAR(100),
    extraction_source VARCHAR(50),
    extraction_date TIMESTAMP,
    PRIMARY KEY (id, extraction_date)
);

CREATE TABLE IF NOT EXISTS staging_sales (
    transaction_id VARCHAR(50),
    product_id VARCHAR(50),
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    sale_date DATE,
    customer_id VARCHAR(50),
    extraction_source VARCHAR(50),
    extraction_date TIMESTAMP,
    PRIMARY KEY (transaction_id, extraction_date)
);

CREATE TABLE IF NOT EXISTS staging_profiles (
    user_id VARCHAR(50),
    full_name VARCHAR(100),
    age INTEGER,
    preferences JSONB,
    last_login TIMESTAMP,
    extraction_source VARCHAR(50),
    extraction_date TIMESTAMP,
    PRIMARY KEY (user_id, extraction_date)
);

CREATE TABLE IF NOT EXISTS staging_events (
    event_id VARCHAR(50),
    event_type VARCHAR(50),
    user_id VARCHAR(50),
    timestamp TIMESTAMP,
    value DECIMAL(10,2),
    extraction_source VARCHAR(50),
    extraction_date TIMESTAMP,
    PRIMARY KEY (event_id, extraction_date)
);