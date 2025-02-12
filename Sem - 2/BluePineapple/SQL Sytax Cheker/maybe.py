import re

# Define token types
TOKEN_TYPES = {
    "KEYWORD": r"\b(SELECT|FROM|WHERE|INSERT|INTO|VALUES|UPDATE|SET|DELETE)\b",
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "SYMBOL": r"[(),=<>;*]",
    "VALUE": r"'[^']*'|\d+"
}

class SQLParser:
    def __init__(self, query):
        self.tokens = self.tokenize(query)
        self.index = 0
    
    def tokenize(self, sql):
        sql = re.sub(r"\s+", " ", sql.strip())
        sql = sql.upper()  # Convert SQL to uppercase for case insensitivity
        tokens = []
        pattern = "|".join(f"(?P<{key}>{value})" for key, value in TOKEN_TYPES.items())
        
        for match in re.finditer(pattern, sql):
            token_type = match.lastgroup
            value = match.group().strip()
            tokens.append((token_type, value))
        
        tokens.append(("END", ""))  # End of token list
        return tokens
    
    def match(self, expected_type, expected_value=None):
        if self.index < len(self.tokens):
            token_type, token_value = self.tokens[self.index]
            if token_type == expected_type and (expected_value is None or token_value == expected_value):
                self.index += 1
                return token_value
        return None
    
    def parse_select(self):
        if not self.match("KEYWORD", "SELECT"):
            return "Syntax Error: Expected 'SELECT'!"
        
        if not self.match("IDENTIFIER") and not self.match("SYMBOL", "*"):
            return "Syntax Error: Expected at least one column or '*' after 'SELECT'!"
        
        while self.match("SYMBOL", ","):
            if not self.match("IDENTIFIER"):
                return "Syntax Error: Expected column name after ','!"
        
        if not self.match("KEYWORD", "FROM"):
            return "Syntax Error: Missing 'FROM'!"
        
        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name!"
        
        if self.match("KEYWORD", "WHERE"):
            if not self.match("IDENTIFIER") or not self.match("SYMBOL", "=") or not self.match("VALUE"):
                return "Syntax Error: Invalid WHERE clause!"
        
        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"
        
        return "Valid SELECT syntax!"
    
    def parse_insert(self):
        if not self.match("KEYWORD", "INSERT") or not self.match("KEYWORD", "INTO"):
            return "Syntax Error: Expected 'INSERT INTO'!"
        
        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name!"
        
        if self.match("SYMBOL", "("):
            while self.match("IDENTIFIER") or self.match("SYMBOL", ","):
                pass
            if not self.match("SYMBOL", ")"):
                return "Syntax Error: Expected ')' after column names!"
        
        if not self.match("KEYWORD", "VALUES"):
            return "Syntax Error: Expected 'VALUES'!"
        
        if not self.match("SYMBOL", "("):
            return "Syntax Error: Expected '(' before values!"
        
        while self.match("VALUE") or self.match("SYMBOL", ","):
            pass
        
        if not self.match("SYMBOL", ")"):
            return "Syntax Error: Expected ')' after values!"
        
        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"
        
        return "Valid INSERT syntax!"
    
    def parse_update(self):
        if not self.match("KEYWORD", "UPDATE"):
            return "Syntax Error: Expected 'UPDATE'!"
        
        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name!"
        
        if not self.match("KEYWORD", "SET"):
            return "Syntax Error: Expected 'SET'!"
        
        while self.match("IDENTIFIER") and self.match("SYMBOL", "=") and self.match("VALUE"):
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
            return "Syntax Error: Expected 'DELETE'!"
        
        if not self.match("KEYWORD", "FROM"):
            return "Syntax Error: Missing 'FROM'!"
        
        if not self.match("IDENTIFIER"):
            return "Syntax Error: Missing table name!"
        
        if self.match("KEYWORD", "WHERE"):
            if not self.match("IDENTIFIER") or not self.match("SYMBOL", "=") or not self.match("VALUE"):
                return "Syntax Error: Invalid WHERE clause!"
        
        if not self.match("SYMBOL", ";"):
            return "Syntax Error: Query must end with ';'!"
        
        return "Valid DELETE syntax!"
    
    def parse(self):
        if self.tokens[0][1] == "SELECT":
            return self.parse_select()
        elif self.tokens[0][1] == "INSERT":
            return self.parse_insert()
        elif self.tokens[0][1] == "UPDATE":
            return self.parse_update()
        elif self.tokens[0][1] == "DELETE":
            return self.parse_delete()
        return "Syntax Error: Unsupported SQL statement!"


while True:
    query = input("Enter SQL query: ")
    if not query:
        break
    
    parser = SQLParser(query)
    result = parser.parse()
    print(result)