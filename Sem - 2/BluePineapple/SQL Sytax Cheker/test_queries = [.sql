test_queries = [
    "SELECT name ,age FROM users;",  # Invalid: Missing comma
    "INSERT INTO employees (id, name) VALUES (1, 'John');",  # Valid
    "UPDATE customers email='test@example.com' WHERE id=5;",  # Invalid: Missing SET keyword
    "DELETE FROM orders WHERE order_id=10;",  # Valid
    "ALTER TABLE employees DROP COLUMN age;",  # Valid
    "CREATE TABLE books (id INT PRIMARY KEY, title VARCHAR(100));",  # Valid
    "DROP temp_data;",  # Invalid: Missing TABLE keyword
    "TRUNCATE TABLE logs;",  # Valid
    "SELECT COUNT(*) FROM orders;",  # Valid
    "INSERT INTO users username, email VALUES ('john', 'john@example.com');",  # Invalid: Missing parentheses
    "UPDATE users SET last_login WHERE id=42;",  # Invalid: Missing value assignment
    "DELETE FROM users WHERE last_login < '2023-01-01';",  # Valid
    "ALTER TABLE customers MODIFY COLUMN email VARCHAR(255);",  # Valid
    "CREATE TABLE (id INT, name VARCHAR(100));",  # Invalid: Missing table name
    "DROP TABLE archived_orders;",  # Valid
    "TRUNCATE FROM users;",  # Invalid: Incorrect syntax
    "SELECT * FROM employees;",  # Valid
    "INSERT INTO books VALUES 10, 'Harry Potter', 'J.K. Rowling';",  # Invalid: Missing parentheses
    "UPDATE products SET price = 19.99 WHERE category = 'Books';",  # Valid
    "DELETE users WHERE last_login < '2023-01-01';",  # Invalid: Missing FROM keyword
    "ALTER TABLE products ADD price DECIMAL(10,2);",  # Invalid: Missing COLUMN keyword
    "CREATE TABLE students (student_id INT, name VARCHAR(100), age INT, PRIMARY KEY(student_id));",  # Valid
    "DROP TABLE old_logs;",  # Valid
    "TRUNCATE TABLE old_data;",  # Valid
    "SELECT name, FROM employees;",  # Invalid: Trailing comma
    "INSERT INTO clients (id, name, country) VALUES (NULL, 'Alice', 'USA');",  # Valid
    "UPDATE employees SET name = 'Alice' department = 'HR' WHERE id = 1;",  # Invalid: Missing comma in SET clause
    "DELETE FROM logs WHERE event_type = 'ERROR';",  # Valid
    "ALTER products MODIFY email VARCHAR(255);",  # Invalid: Missing TABLE keyword
    "CREATE TABLE transactions (txn_id INT, amount FLOAT, txn_date DATE);",  # Valid
    "DROP TABLE expired_tokens;",  # Valid
    "TRUNCATE TABLE failed_payments;",  # Valid
    "SELECT DISTINCT city FROM locations;",  # Valid
    "SELECT * FROM WHERE id = 5;",  # Invalid: Missing table name
    "UPDATE orders SET status 'Shipped' WHERE order_id=500;",  # Invalid: Missing equal sign
    "DELETE FROM logs WHERE = 'ERROR';",  # Invalid: Missing column name
    "ALTER TABLE users RENAME COLUMN username TO user_name;",  # Valid
    "CREATE books (id INT, title VARCHAR(100));",  # Invalid: Missing TABLE keyword
    "DROP TABLE obsolete_records;",  # Valid
    "TRUNCATE TABLE temporary_results;",  # Valid
    "SELECT id, name FROM products WHERE price > 100 AND category = 'Electronics';",  # Valid
    "SELECT id name FROM customers;",  # Invalid: Missing comma
    "INSERT INTO orders (order_id, customer_id, amount) VALUES (1001, 5, 250.75);",  # Valid
    "UPDATE employees SET department = 'HR' WHERE name = 'Alice';",  # Valid
    "DELETE FROM WHERE order_id=10;",  # Invalid: Missing table name
    "ALTER TABLE users DROP username;",  # Invalid: Missing COLUMN keyword
    "CREATE TABLE inventory (id INT, item_name VARCHAR(255), quantity INT, price DECIMAL(8,2));",  # Valid
    "DROP TABLE IF EXISTS;",  # Invalid: Missing table name
    "TRUNCATE TABLE sessions;",  # Valid
    "SELECT name FROM students WHERE age > 18 ORDER BY name;",  # Valid
    "INSERT INTO customers (id, name) VALUES (NULL, 'Alice', 'USA');",  # Valid
    "UPDATE orders SET status = 'Shipped', tracking_number = 'ABC123' WHERE order_id = 500;",  # Valid
    "DELETE FROM books WHERE title = 'Outdated Book';",  # Valid
    "ALTER TABLE books CHANGE title book_title VARCHAR(200);",  # Valid
    "CREATE TABLE orders (id INT, PRIMARY KEY id);",  # Invalid: Incorrect PRIMARY KEY syntax
    "DROP TABLE expired_tokens;",  # Valid
    "SELECT id FROM customers WHERE email = 'test@example.com';",  # Valid
    "INSERT INTO employees (id, name) VALUES (1, 'John');",  # Valid
    "UPDATE customers email='test@example.com' WHERE id=5;",  # Invalid: Missing SET keyword
    "DELETE FROM orders WHERE order_id=10;",  # Valid
    "ALTER TABLE employees DROP COLUMN age;",  # Valid
    "CREATE TABLE books (id INT PRIMARY KEY, title VARCHAR(100));",  # Valid
    "DROP temp_data;",  # Invalid: Missing TABLE keyword
    "TRUNCATE TABLE logs;",  # Valid
    "SELECT COUNT(*) FROM orders;",  # Valid
    "INSERT INTO users username, email VALUES ('john', 'john@example.com');",  # Invalid: Missing parentheses
    "UPDATE users SET last_login WHERE id=42;",  # Invalid: Missing value assignment
    "DELETE FROM users WHERE last_login < '2023-01-01';",  # Valid
    "ALTER TABLE customers MODIFY COLUMN email VARCHAR(255);",  # Valid
    "CREATE TABLE (id INT, name VARCHAR(100));",  # Invalid: Missing table name
    "DROP TABLE archived_orders;",  # Valid
    "TRUNCATE FROM users;",  # Invalid: Incorrect syntax
    "SELECT * FROM employees;",  # Valid
    "INSERT INTO books VALUES 10, 'Harry Potter', 'J.K. Rowling';",  # Invalid: Missing parentheses
    "UPDATE products SET price = 19.99 WHERE category = 'Books';",  # Valid
    "DELETE users WHERE last_login < '2023-01-01';",  # Invalid: Missing FROM keyword
    "ALTER TABLE products ADD price DECIMAL(10,2);",  # Invalid: Missing COLUMN keyword
    "CREATE TABLE students (student_id INT, name VARCHAR(100), age INT, PRIMARY KEY(student_id));",  # Valid
    "DROP TABLE old_logs;",  # Valid
    "TRUNCATE TABLE old_data;",  # Valid
    "SELECT name, FROM employees;",  # Invalid: Trailing comma
    "INSERT INTO clients (id, name, country) VALUES (NULL, 'Alice', 'USA');",  # Valid
    "UPDATE employees SET name = 'Alice' department = 'HR' WHERE id = 1;",  # Invalid: Missing comma in SET clause
    "DELETE FROM logs WHERE event_type = 'ERROR';",  # Valid
    "ALTER products MODIFY email VARCHAR(255);",  # Invalid: Missing TABLE keyword
    "CREATE TABLE transactions (txn_id INT, amount FLOAT, txn_date DATE);",  # Valid
    "DROP TABLE expired_tokens;",  # Valid
    "TRUNCATE TABLE failed_payments;",  # Valid,
    "SELECT DISTINCT city FROM locations;",  # Valid
    "SELECT * FROM WHERE id = 5;",  # Invalid: Missing table name
    "UPDATE orders SET status 'Shipped' WHERE order_id=500;",  # Invalid: Missing equal sign
    "DELETE FROM logs WHERE = 'ERROR';",  # Invalid: Missing column name
    "ALTER TABLE users RENAME COLUMN username TO user_name;",  # Valid
    "CREATE books (id INT, title VARCHAR(100));",  # Invalid: Missing TABLE keyword
    "DROP TABLE obsolete_records;",  # Valid
    "TRUNCATE TABLE temporary_results;"  # Valid
]
