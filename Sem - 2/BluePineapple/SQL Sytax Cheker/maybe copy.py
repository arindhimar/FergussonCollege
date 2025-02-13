import re

class SQLParser:
    def __init__(self, query):
        self.query = query.strip()
        self.tokens = self.tokenize(query)
        self.current_token_index = 0

    def tokenize(self, query):
        pattern = r'([(),;*])|([<>!=]=?)|\b(SELECT|FROM|WHERE|INSERT INTO|VALUES|UPDATE|SET|DELETE FROM|CREATE TABLE|ALTER TABLE|DROP TABLE|TRUNCATE TABLE|ADD COLUMN|RENAME COLUMN|CHANGE COLUMN|MODIFY COLUMN|AND|OR|NOT|NULL|IN|LIKE|COUNT|SUM|AVG|MIN|MAX)\b'
        tokens = [token for token in re.split(pattern, query, flags=re.IGNORECASE) if token and token.strip()]
        return [token.upper() if token.upper() in {'SELECT', 'FROM', 'WHERE', 'INSERT INTO', 'VALUES', 'UPDATE', 'SET', 'DELETE FROM', 'CREATE TABLE', 'ALTER TABLE', 'DROP TABLE', 'TRUNCATE TABLE', 'ADD COLUMN', 'RENAME COLUMN', 'CHANGE COLUMN', 'MODIFY COLUMN', 'AND', 'OR', 'NOT', 'NULL', 'IN', 'LIKE', 'COUNT', 'SUM', 'AVG', 'MIN', 'MAX'} else token for token in tokens]
    
    def match(self, expected):
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index] == expected:
            self.current_token_index += 1
            return True
        return False
    
    def expect(self, expected):
        if not self.match(expected):
            raise SyntaxError(f"Expected '{expected}' but found '{self.tokens[self.current_token_index]}'")
    
    def parse_select(self):
        self.expect('SELECT')
        if self.match('COUNT') or self.match('SUM') or self.match('AVG') or self.match('MIN') or self.match('MAX'):
            self.expect('(')
            self.expect(self.tokens[self.current_token_index])  # Expect column name
            self.expect(')')
        else:
            self.expect('*')  # Can be extended to handle column lists
        self.expect('FROM')
        self.expect(self.tokens[self.current_token_index])  # Expect table name
        if self.match('WHERE'):
            self.expect(self.tokens[self.current_token_index])  # Expect column name
            self.expect('=')  # Expect comparison operator
            self.expect(self.tokens[self.current_token_index])  # Expect value
        if self.match(';'):
            return "Valid SELECT syntax!"
        raise SyntaxError(f"Unexpected token: '{self.tokens[self.current_token_index]}'")
    
    def parse_insert(self):
        self.expect('INSERT INTO')
        self.expect(self.tokens[self.current_token_index])  # Expect table name
        self.expect('VALUES')
        self.expect('(')
        self.expect(self.tokens[self.current_token_index])  # Expect values
        self.expect(')')
        if self.match(';'):
            return "Valid INSERT syntax!"
        raise SyntaxError(f"Unexpected token: '{self.tokens[self.current_token_index]}'")
    
    def parse_update(self):
        self.expect('UPDATE')
        self.expect(self.tokens[self.current_token_index])  # Expect table name
        self.expect('SET')
        self.expect(self.tokens[self.current_token_index])  # Expect column name
        self.expect('=')  # Ensure assignment operator is present
        self.expect(self.tokens[self.current_token_index])  # Expect value after '='
        if self.match('WHERE'):
            self.expect(self.tokens[self.current_token_index])  # Expect column name
            self.expect('=')  # Expect comparison operator
            self.expect(self.tokens[self.current_token_index])  # Expect value
        if self.match(';'):
            return "Valid UPDATE syntax!"
        raise SyntaxError(f"Unexpected token: '{self.tokens[self.current_token_index]}'")
    
    def parse_delete(self):
        self.expect('DELETE FROM')
        self.expect(self.tokens[self.current_token_index])  # Expect table name
        if self.match('WHERE'):
            self.expect(self.tokens[self.current_token_index])  # Expect column name
            self.expect('=')  # Expect comparison operator
            self.expect(self.tokens[self.current_token_index])  # Expect value
        if self.match(';'):
            return "Valid DELETE syntax!"
        raise SyntaxError(f"Unexpected token: '{self.tokens[self.current_token_index]}'")
    
    def parse_ddl(self):
        ddl_type = self.tokens[0]
        self.expect(ddl_type)  # CREATE TABLE, ALTER TABLE, DROP TABLE, etc.
        self.expect(self.tokens[self.current_token_index])  # Expect table name
        if ddl_type == 'ALTER TABLE':
            self.expect('ADD COLUMN')
            self.expect(self.tokens[self.current_token_index])  # Expect column name
        if self.match(';'):
            return f"Valid {ddl_type} syntax!"
        raise SyntaxError(f"Unexpected token: '{self.tokens[self.current_token_index]}'")
    
    def parse(self):
        try:
            first_token = self.tokens[0].upper()
            if first_token == 'SELECT':
                return self.parse_select()
            elif first_token == 'INSERT INTO':
                return self.parse_insert()
            elif first_token == 'UPDATE':
                return self.parse_update()
            elif first_token == 'DELETE FROM':
                return self.parse_delete()
            elif first_token in {'CREATE TABLE', 'ALTER TABLE', 'DROP TABLE', 'TRUNCATE TABLE'}:
                return self.parse_ddl()
            else:
                return "Invalid or unsupported SQL statement!"
        except SyntaxError as e:
            return f"Syntax Error: {str(e)}"

if __name__ == "__main__":
    queries = [
        "SELECT COUNT(*) FROM users;",
        "SELECT SUM(price) FROM products;",
        "SELECT AVG(age) FROM customers;",
        "SELECT MIN(salary) FROM employees;",
        "SELECT MAX(score) FROM exams;",
        "DELETE FROM orders WHERE order_id = 10;",
        "UPDATE users SET last_login WHERE id=42;"  # Now should correctly detect missing assignment
    ]
    
    for query in queries:
        parser = SQLParser(query)
        print(parser.parse())
