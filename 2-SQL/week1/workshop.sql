-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'week1_workshop' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS week1_workshop;
CREATE DATABASE week1_workshop;
-- connect via psql
\c week1_workshop

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


---
--- CREATE tables
---

CREATE TABLE products (
    id SERIAL,
    name TEXT NOT NULL,
    discontinued BOOLEAN NOT NULL,
    supplier_id INT,
    category_id INT,
    PRIMARY KEY(id)
);


CREATE TABLE categories (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    picture TEXT,
    PRIMARY KEY (id)
);

-- TODO create more tables here...


---
--- Add foreign key constraints
---

ALTER TABLE products
ADD CONSTRAINT fk_products_categories
FOREIGN KEY (category_id)
REFERENCES categories;

-- TODO create more constraints here...




-- Write SQL that creates a table named suppliers which represents the Supplier entity.

CREATE TABLE suppliers (
    id SERIAL,
    name TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE customers (
    id SERIAL,
    company_name TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE employees (
    id SERIAL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    reports_to INT,
    PRIMARY KEY (id)
);

CREATE TABLE orders (
    id SERIAL,
    date DATE,
    customers_id INT,
    employees_id INT,
    PRIMARY KEY (id)
);

CREATE TABLE orders_products (
    orders_id INT,
    products_id INT,
    discount NUMERIC,
    quantity INT NOT NULL,
    PRIMARY KEY (orders_id, products_id)
);

CREATE TABLE territories (
    id SERIAL,
    description TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE employees_territories (
    employees_id INT,
    territories_id INT,
    PRIMARY KEY (employees_id, territories_id)
);

CREATE TABLE offices (
    id SERIAL,
    territories_id INT,
    address_line TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE us_states (
    id SERIAL,
    abbrevation char(2) UNIQUE NOT NULL,
    name TEXT UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customers_id)
REFERENCES customers;

ALTER TABLE orders
ADD CONSTRAINT fk_orders_employees
FOREIGN KEY (employees_id)
REFERENCES employees;

-- ONE TO MANY -- since one existed I guess
ALTER TABLE products
ADD CONSTRAINT fk_products_suppliers
FOREIGN KEY (supplier_id)
REFERENCES suppliers;

-- MANY TO MANY --
ALTER TABLE orders_products
ADD CONSTRAINT fk_orders_products_orders
FOREIGN KEY (orders_id)
REFERENCES orders;

ALTER TABLE orders_products
ADD CONSTRAINT fk_orders_products_products
FOREIGN KEY (products_id)
REFERENCES products;


-- MANY TO MANY --
ALTER TABLE employees_territories
ADD CONSTRAINT fk_employees_territories_employees
FOREIGN KEY (employees_id)
REFERENCES employees;

ALTER TABLE employees_territories
ADD CONSTRAINT fk_employees_territories_territories
FOREIGN KEY (territories_id)
REFERENCES territories;

-- ONE TO ONE --
ALTER TABLE offices
ADD CONSTRAINT fk_offices_territories
FOREIGN KEY (territories_id)
REFERENCES territories;

-- BONUS
ALTER TABLE employees
ADD CONSTRAINT fk_employees_reports_to
FOREIGN KEY (reports_to)
REFERENCES employees;