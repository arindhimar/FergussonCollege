import re

# Define token types
TOKEN_TYPES = {
    "KEYWORD": r"\b(SELECT|FROM|WHERE|INSERT|INTO|VALUES|UPDATE|SET|DELETE|ORDER BY|GROUP BY|HAVING|AND|OR|NOT|NULL|IN|LIKE|DISTINCT|AS)\b",
    "AGGREGATE": r"\b(COUNT|SUM|AVG|MIN|MAX)\b",  # Aggregate functions
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "SYMBOL": r"[(),=<>;*!=]",  
    "VALUE": r"'[^']*'|\d+"  
}


class SQLParser:
    def __init__(self, query):
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

    def parse_select(self):
        """Parses and validates a SELECT statement, handling aggregate functions, WHERE, ORDER BY, and GROUP BY."""

        if not self.match("KEYWORD", "SELECT"):
            return "Syntax Error: Expected 'SELECT' keyword!"

        expect_column = True  # Expecting either a column name or aggregate function
        has_aggregate = False  # Track if an aggregate function is used

        while expect_column:
            # Handle Aggregate Functions (COUNT, SUM, AVG, MIN, MAX)
            if self.match("AGGREGATE"):
                has_aggregate = True  # Mark aggregate function usage
                if not self.match("SYMBOL", "("):
                    return "Syntax Error: Expected '(' after aggregate function!"
                if not self.match("IDENTIFIER") and not self.match("SYMBOL", "*"):
                    return "Syntax Error: Expected column name or '*' inside aggregate function!"
                if not self.match("SYMBOL", ")"):
                    return "Syntax Error: Expected ')' after column name in aggregate function!"

            # Handle Regular Columns
            elif not self.match("IDENTIFIER") and not self.match("SYMBOL", "*"):
                return "Syntax Error: Expected column names, '*' or aggregate function after 'SELECT'!"

            # Check for additional columns (comma-separated)
            if self.match("SYMBOL", ","):
                expect_column = True  # Another column/aggregate expected after ','
            else:
                expect_column = False  # No more columns

        # Ensure FROM clause is present **after column selection**
        if not self.match("KEYWORD", "FROM"):
            return "Syntax Error: Expected 'FROM' keyword after column selection!"

        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name after 'FROM'!"

        # Handle optional WHERE clause
        if self.match("KEYWORD", "WHERE"):
            while True:
                if not self.match("IDENTIFIER"):
                    return "Syntax Error: Expected column name after 'WHERE'!"
                if not (self.match("SYMBOL", "=") or self.match("SYMBOL", "<") or self.match("SYMBOL", ">") or self.match("SYMBOL", "!=")):
                    return "Syntax Error: Expected comparison operator (=, <, >, !=) in WHERE clause!"
                if not self.match("VALUE"):
                    return "Syntax Error: Missing value after comparison operator in WHERE clause!"

                # Handle multiple conditions (AND, OR)
                if not self.match("KEYWORD", "AND") and not self.match("KEYWORD", "OR"):
                    break  # Stop processing WHERE clause if no AND/OR is found

        # Handle optional GROUP BY clause
        if self.match("KEYWORD", "GROUP"):
            if not self.match("KEYWORD", "BY"):
                return "Syntax Error: Expected 'BY' after 'GROUP'!"
            if not self.match("IDENTIFIER"):
                return "Syntax Error: Expected column name after 'GROUP BY'!"

        # Handle optional ORDER BY clause
        if self.match("KEYWORD", "ORDER"):
            if not self.match("KEYWORD", "BY"):
                return "Syntax Error: Expected 'BY' after 'ORDER'!"
            if not self.match("IDENTIFIER"):
                return "Syntax Error: Expected column name after 'ORDER BY'!"

            # Optional ASC/DESC sorting
            if self.match("KEYWORD", "ASC") or self.match("KEYWORD", "DESC"):
                pass

        # ✅ **Fix: Now check for the semicolon properly at the end**
        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"

        return "Valid SELECT syntax!"

    
    def parse_insert(self):
        if not self.match("KEYWORD", "INSERT"):
            return "Syntax Error: Expected 'INSERT' keyword!"

        if not self.match("KEYWORD", "INTO"):
            return "Syntax Error: Expected 'INTO' after 'INSERT'!"

        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name after 'INSERT INTO'!"

        # Optional column list (INSERT INTO table (col1, col2) VALUES (...))
        column_count = 0
        if self.match("SYMBOL", "("):
            while self.match("IDENTIFIER"):
                column_count += 1  # Count columns
                if not self.match("SYMBOL", ","):  # If no comma, break loop
                    break
            if not self.match("SYMBOL", ")"):
                return "Syntax Error: Expected ')' after column names!"

        # Ensure VALUES keyword is present
        if not self.match("KEYWORD", "VALUES"):
            return "Syntax Error: Expected 'VALUES' keyword!"

        # Handle values inside parentheses
        if not self.match("SYMBOL", "("):
            return "Syntax Error: Expected '(' before values!"

        value_count = 0
        while self.match("VALUE"):
            value_count += 1  # Count values
            if not self.match("SYMBOL", ","):  # If no comma, break loop
                break

        if not self.match("SYMBOL", ")"):
            return "Syntax Error: Expected ')' after values!"

        # Ensure column count matches value count (if columns are explicitly mentioned)
        if column_count > 0 and column_count != value_count:
            return f"Syntax Error: Expected {column_count} values, but found {value_count}!"

        # Ensure query ends with semicolon
        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"

        return "Valid INSERT syntax!"


    def parse_update(self):
        if not self.match("KEYWORD", "UPDATE"):
            return "Syntax Error: Expected 'UPDATE' keyword!"

        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name after 'UPDATE'!"

        if not self.match("KEYWORD", "SET"):
            return "Syntax Error: Expected 'SET' keyword!"

        # Ensure at least one column assignment exists (column = value)
        has_assignment = False
        while self.match("IDENTIFIER"):
            if not self.match("SYMBOL", "="):
                return "Syntax Error: Expected '=' in SET clause!"

            if not self.match("VALUE"):
                return "Syntax Error: Missing value assignment in SET clause!"

            has_assignment = True  # At least one valid assignment found

            if not self.match("SYMBOL", ","):  # If no comma, break loop
                break

        if not has_assignment:
            return "Syntax Error: SET clause must have at least one 'column = value' pair!"

        # Handle optional WHERE clause
        if self.match("KEYWORD", "WHERE"):
            if not self.match("IDENTIFIER"):
                return "Syntax Error: Expected column name after 'WHERE'!"
            
            if not (self.match("SYMBOL", "=") or self.match("SYMBOL", "<") or self.match("SYMBOL", ">") or self.match("SYMBOL", "!=")):
                return "Syntax Error: Expected comparison operator (=, <, >, !=) in WHERE clause!"
            
            if not self.match("VALUE"):
                return "Syntax Error: Missing value after comparison operator in WHERE clause!"

        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"

        return "Valid"

    def parse_delete(self):
        if not self.match("KEYWORD", "DELETE"):
            return "Syntax Error: Expected 'DELETE' keyword!"

        if not self.match("KEYWORD", "FROM"):
            return "Syntax Error: Expected 'FROM' after 'DELETE'!"

        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name after 'FROM'!"

        # Handle optional WHERE clause
        if self.match("KEYWORD", "WHERE"):
            if not self.match("IDENTIFIER"):
                return "Syntax Error: Expected column name after 'WHERE'!"

            if not (self.match("SYMBOL", "=") or self.match("SYMBOL", "<") or self.match("SYMBOL", ">") or self.match("SYMBOL", "!=")):
                return "Syntax Error: Expected comparison operator (=, <, >, !=) in WHERE clause!"

            if not self.match("VALUE"):
                return "Syntax Error: Missing value after comparison operator in WHERE clause!"

        # Ensure query ends with a semicolon
        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"

        return "Valid DELETE syntax!"

    def match(self, expected_type, expected_value=None):
        if self.index < len(self.tokens):
            token_type, token_value = self.tokens[self.index]
            if token_type == expected_type and (expected_value is None or token_value == expected_value):
                self.index += 1
                return token_value
        return None

    def parse(self):
        first_token = self.tokens[0][1]
        if first_token == "SELECT":
            return self.parse_select()
        elif first_token == "INSERT":
            return self.parse_insert()
        elif first_token == "UPDATE":
            return self.parse_update()
        elif first_token == "DELETE":
            return self.parse_delete()
        return "Unsupported"

while True:
    query = input("Enter a SQL query (or 'exit' to quit): ")
    if query.lower() == "exit":
        break

    parser = SQLParser(query)
    result = parser.parse()
    print(result)