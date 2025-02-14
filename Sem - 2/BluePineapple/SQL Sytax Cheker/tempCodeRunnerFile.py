    test_cases = [
        "DELETE FROM customers WHERE name IN ('Alice', 'Bob');",  # Valid
        "DELETE FROM customers WHERE name IN (\"Alice\", \"Bob\";",  # Invalid
        "ALTER TABLE table_name ADD int int;;",  # Invalid
        "DELETE FROM users WHERE id IN (1, 'Bob, Charlie');",  # Valid
        "SELECT * FROM orders WHERE date > '2023-01-01';"  # Valid
    ]
