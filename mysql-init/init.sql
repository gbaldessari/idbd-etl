CREATE DATABASE IF NOT EXISTS ecommerce_db;
CREATE USER IF NOT EXISTS 'etl_user'@'%' IDENTIFIED BY 'etl_password';
GRANT ALL PRIVILEGES ON ecommerce_db.* TO 'etl_user'@'%';
FLUSH PRIVILEGES;

USE ecommerce_db;
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    registration_date TIMESTAMP
);

INSERT INTO customers (customer_id, first_name, last_name, email, registration_date)
VALUES 
    ('CUST001', 'John', 'Doe', 'john.doe@example.com', NOW() - INTERVAL 5 DAY),
    ('CUST002', 'Jane', 'Smith', 'jane.smith@example.com', NOW() - INTERVAL 3 DAY),
    ('CUST003', 'Robert', 'Johnson', 'robert.j@example.com', NOW() - INTERVAL 1 DAY);