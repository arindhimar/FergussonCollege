import re

# Define token types
TOKEN_TYPES = {
    "KEYWORD": r"\b(SELECT|FROM|WHERE|INSERT|INTO|VALUES|UPDATE|SET|DELETE|COUNT|SUM|AVG|MIN|MAX|DROP|TABLE|CREATE|PRIMARY|KEY|NOT|NULL|UNIQUE|VARCHAR|INT|FLOAT|CHAR|TEXT)\b",
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "SYMBOL": r"[(),=<>;*!]",
    "VALUE": r"'[^']*'|\d+"
}

class SQLParser:
    def _init_(self, query):
        self.original_query = query.strip()
        self.tokens = self.tokenize(query)
        self.index = 0

    def tokenize(self, sql):
        sql = re.sub(r"\s+", " ", sql.strip())
        sql = sql.upper()  # Convert to uppercase for case insensitivity
        tokens = []
        pattern = "|".join(f"(?P<{key}>{value})" for key, value in TOKEN_TYPES.items())

        for match in re.finditer(pattern, sql):
            token_type = match.lastgroup
            value = match.group().strip()
            tokens.append((token_type, value))

        tokens.append(("END", ""))  # End of token list
        return tokens

    def parse_create(self):
        if not self.match("KEYWORD", "CREATE"):
            return "Syntax Error: Expected 'CREATE' keyword!"
        
        if not self.match("KEYWORD", "TABLE"):
            return "Syntax Error: Expected 'TABLE' keyword after 'CREATE'!"
        
        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name after 'CREATE TABLE'!"

        if not self.match("SYMBOL", "("):
            return "Syntax Error: Expected '(' after table name!"
        
        column_count = 0
        while self.match("IDENTIFIER"):  # Column name
            column_count += 1
            
            if not self.match("KEYWORD"):  
                return "Syntax Error: Expected data type after column name!"

            if self.tokens[self.index - 1][1] in ["VARCHAR", "CHAR"]:
                if not self.match("SYMBOL", "(") or not self.match("VALUE") or not self.match("SYMBOL", ")"):
                    return "Syntax Error: Expected '(size)' after VARCHAR or CHAR!"

            while self.match("KEYWORD", "PRIMARY") or self.match("KEYWORD", "NOT") or self.match("KEYWORD", "UNIQUE"):
                if self.match("KEYWORD", "KEY"):
                    continue
                if self.match("KEYWORD", "NULL"):
                    continue

            if not self.match("SYMBOL", ","):  # If there's a comma, expect more columns
                break

        if column_count == 0:
            return "Syntax Error: At least one column definition is required!"

        if not self.match("SYMBOL", ")"):
            return "Syntax Error: Expected ')' after column definitions!"
        
        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"

        return "Valid CREATE TABLE syntax!"

    def parse_select(self):
        if not self.match("KEYWORD", "SELECT"):
            return "Syntax Error: Expected 'SELECT' keyword!"

        if not self.match("IDENTIFIER") and not self.match("SYMBOL", "*"):
            return "Syntax Error: Expected column names or '*' after 'SELECT'!"

        while self.match("SYMBOL", ","):
            if not self.match("IDENTIFIER"):
                return "Syntax Error: Expected column name after ','!"

        if not self.match("KEYWORD", "FROM"):
            return "Syntax Error: Expected 'FROM' keyword!"

        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name!"

        if self.match("KEYWORD", "WHERE"):
            if not self.match("IDENTIFIER"):
                return "Syntax Error: Expected column name after 'WHERE'!"
            if not self.match("SYMBOL", "="):
                return "Syntax Error: Expected '=' after column name!"
            if not self.match("VALUE"):
                return "Syntax Error: Missing value!"

        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"

        return "Valid SELECT syntax!"

    def parse_insert(self):
        if not self.match("KEYWORD", "INSERT"):
            return "Syntax Error: Expected 'INSERT' keyword!"

        if not self.match("KEYWORD", "INTO"):
            return "Syntax Error: Expected 'INTO' after 'INSERT'!"

        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name!"

        if not self.match("KEYWORD", "VALUES"):
            return "Syntax Error: Expected 'VALUES' keyword!"

        if not self.match("SYMBOL", "("):
            return "Syntax Error: Expected '(' before values!"

        while self.match("VALUE"):
            if not self.match("SYMBOL", ","):
                break

        if not self.match("SYMBOL", ")"):
            return "Syntax Error: Expected ')' after values!"

        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"

        return "Valid INSERT syntax!"

    def parse_update(self):
        if not self.match("KEYWORD", "UPDATE"):
            return "Syntax Error: Expected 'UPDATE' keyword!"

        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name!"

        if not self.match("KEYWORD", "SET"):
            return "Syntax Error: Expected 'SET' keyword!"

        while self.match("IDENTIFIER"):
            if not self.match("SYMBOL", "="):
                return "Syntax Error: Expected '='!"
            if not self.match("VALUE"):
                return "Syntax Error: Expected value!"
            if not self.match("SYMBOL", ","):
                break

        if self.match("KEYWORD", "WHERE"):
            if not self.match("IDENTIFIER") or not self.match("SYMBOL", "=") or not self.match("VALUE"):
                return "Syntax Error: Invalid WHERE clause!"

        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"

        return "Valid UPDATE syntax!"

    def parse_delete(self):
        if not self.match("KEYWORD", "DELETE"):
            return "Syntax Error: Expected 'DELETE' keyword!"

        if not self.match("KEYWORD", "FROM"):
            return "Syntax Error: Expected 'FROM'!"

        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name!"

        if self.match("KEYWORD", "WHERE"):
            if not self.match("IDENTIFIER") or not self.match("SYMBOL", "=") or not self.match("VALUE"):
                return "Syntax Error: Invalid WHERE clause!"

        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"

        return "Valid DELETE syntax!"

    def parse_drop(self):
        if not self.match("KEYWORD", "DROP"):
            return "Syntax Error: Expected 'DROP' keyword!"

        if not self.match("KEYWORD", "TABLE"):
            return "Syntax Error: Expected 'TABLE'!"

        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name!"

        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"

        return "Valid DROP TABLE syntax!"

    def match(self, expected_type, expected_value=None):
        if self.index < len(self.tokens):
            token_type, token_value = self.tokens[self.index]
            if token_type == expected_type and (expected_value is None or token_value == expected_value):
                self.index += 1
                return token_value
        return None

    def parse(self):
        first_token = self.tokens[0][1]
        if first_token == "CREATE":
            return self.parse_create()
        elif first_token == "SELECT":
            return self.parse_select()
        elif first_token == "INSERT":
            return self.parse_insert()
        elif first_token == "UPDATE":
            return self.parse_update()
        elif first_token == "DELETE":
            return self.parse_delete()
        elif first_token == "DROP":
            return self.parse_drop()
        return "Unsupported SQL statement!"

while True:
    query = input("Enter a SQL query (or 'exit' to quit): ")
    if query.lower() == "exit":
        break

    parser = SQLParser(query)
    result = parser.parse()
    print(result)