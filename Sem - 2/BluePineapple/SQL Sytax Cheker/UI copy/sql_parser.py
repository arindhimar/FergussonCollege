import re
from browser import document

class SQLParser:
    def __init__(self, query):
        """Initialize the parser with an SQL query."""
        self.query = query.strip().upper()  # Normalize case
        self.valid = False  # Track if query is valid

    def parse_select(self):
        """Parses a SELECT statement, including aggregate functions, WHERE, GROUP BY, ORDER BY."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Extract clauses using regex
        pattern = (
            r"SELECT\s+(?P<select>.+?)\s+"
            r"FROM\s+(?P<from>\w+)"
            r"(?:\s+WHERE\s+(?P<where>.+?))?"
            r"(?:\s+GROUP BY\s+(?P<group_by>.+?))?"
            r"(?:\s+HAVING\s+(?P<having>.+?))?"
            r"(?:\s+ORDER BY\s+(?P<order_by>.+?))?"
            r"\s*;"
        )
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid SELECT statement structure!"

        self.valid = True
        return "Valid SELECT syntax!"

    def parse_insert(self):
        """Parses an INSERT statement, ensuring correct structure."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"INSERT INTO\s+(?P<table>\w+)\s*(?:$$(?P<columns>.+?)$$)?\s+VALUES\s*$$(?P<values>.+?)$$\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid INSERT statement!"

        self.valid = True
        return "Valid INSERT syntax!"

    def parse_update(self):
        """Parses an UPDATE statement, ensuring it has SET and optionally WHERE."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"UPDATE\s+(?P<table>\w+)\s+SET\s+(?P<set>.+?)(?:\s+WHERE\s+(?P<where>.+?))?\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid UPDATE statement!"

        self.valid = True
        return "Valid UPDATE syntax!"

    def parse_delete(self):
        """Parses a DELETE statement, ensuring FROM is present and optionally WHERE."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"DELETE FROM\s+(?P<table>\w+)(?:\s+WHERE\s+(?P<where>.+?))?\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid DELETE statement!"

        self.valid = True
        return "Valid DELETE syntax!"

    def parse_create(self):
        """Parses a CREATE TABLE statement."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"CREATE TABLE\s+(?P<table>\w+)\s*$$(?P<columns>.+?)$$\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid CREATE TABLE statement!"

        self.valid = True
        return "Valid CREATE TABLE syntax!"

    def parse_alter(self):
        """Parses an ALTER TABLE statement, ensuring proper syntax."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"ALTER TABLE\s+(?P<table>\w+)\s+(?P<action>.+?)\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid ALTER TABLE statement!"

        self.valid = True
        return "Valid ALTER TABLE syntax!"

    def parse_drop(self):
        """Parses a DROP TABLE statement."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"DROP TABLE\s+(?P<table>\w+)\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid DROP TABLE statement!"

        self.valid = True
        return "Valid DROP TABLE syntax!"

    def parse_truncate(self):
        """Parses a TRUNCATE TABLE statement."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"TRUNCATE TABLE\s+(?P<table>\w+)\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid TRUNCATE TABLE statement!"

        self.valid = True
        return "Valid TRUNCATE TABLE syntax!"

    def parse(self):
        """Determines SQL statement type and validates it."""
        first_word = self.query.split()[0]
        if first_word == "SELECT":
            return self.parse_select()
        elif first_word == "INSERT":
            return self.parse_insert()
        elif first_word == "UPDATE":
            return self.parse_update()
        elif first_word == "DELETE":
            return self.parse_delete()
        elif first_word == "CREATE":
            return self.parse_create()
        elif first_word == "ALTER":
            return self.parse_alter()
        elif first_word == "DROP":
            return self.parse_drop()
        elif first_word == "TRUNCATE":
            return self.parse_truncate()
        return "Syntax Error: Unsupported SQL statement!"

def check_syntax(query):
    parser = SQLParser(query)
    return parser.parse()

