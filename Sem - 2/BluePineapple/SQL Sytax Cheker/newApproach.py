import re

class SQLParser:
    def __init__(self, query):
        """Initialize the parser with an SQL query."""
        self.query = query.strip().upper()  # Normalize case
        self.valid = False  # Track if query is valid

    def parse_select(self):
        """Parses a SELECT statement, handling WHERE, GROUP BY, ORDER BY, UNION, INTERSECT."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Support for UNION & INTERSECT
        if " UNION " in self.query or " INTERSECT " in self.query:
            queries = re.split(r" UNION | INTERSECT ", self.query)
            for sub_query in queries:
                if "SELECT" not in sub_query:
                    return "Syntax Error: UNION/INTERSECT must be between SELECT statements!"
                if "FROM" not in sub_query:
                    return "Syntax Error: Missing 'FROM' in UNION/INTERSECT queries!"

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

        clauses = match.groupdict()

        # Validate required parts
        if not clauses["select"] or not clauses["from"]:
            return "Syntax Error: SELECT and FROM are required!"

        # Support for WHERE with IN, NOT IN, BETWEEN, LIKE
        if clauses["where"]:
            where_conditions = clauses["where"].split(" AND ")
            for condition in where_conditions:
                if " IN (" in condition or " NOT IN (" in condition:
                    if not re.match(r"\w+\s+(NOT IN|IN)\s+\(.*\)", condition):
                        return "Syntax Error: Invalid IN/NOT IN syntax!"
                elif " BETWEEN " in condition:
                    if not re.match(r"\w+\s+BETWEEN\s+\S+\s+AND\s+\S+", condition):
                        return "Syntax Error: Invalid BETWEEN syntax!"
                elif " LIKE " in condition:
                    if not re.match(r"\w+\s+LIKE\s+'.*'", condition):
                        return "Syntax Error: Invalid LIKE syntax!"

        self.valid = True
        return "Valid SELECT syntax!"

    def parse_insert(self):
        """Parses an INSERT statement, ensuring correct structure and data validation."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Extract INSERT INTO structure
        pattern = r"INSERT INTO\s+(?P<table>\w+)\s*(?:\((?P<columns>.+?)\))?\s+VALUES\s*\((?P<values>.+?)\)\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid INSERT statement!"

        clauses = match.groupdict()
        table = clauses["table"]
        columns = clauses["columns"]
        values = clauses["values"]

        # Split columns and values
        column_list = [col.strip() for col in columns.split(",")] if columns else []
        value_list = [val.strip() for val in values.split(",")]

        # ✅ Ensure column count matches value count
        if column_list and len(column_list) != len(value_list):
            return f"Syntax Error: Expected {len(column_list)} values, but found {len(value_list)}!"

        # ✅ Validate data types (basic check: numbers should not be enclosed in quotes)
        for val in value_list:
            if re.match(r"^\d+$", val):  # Integer check
                continue  # Valid number
            elif re.match(r"^'.*'$", val):  # Strings should be enclosed in single quotes
                continue  # Valid string
            else:
                return f"Syntax Error: Invalid value format: {val}"

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

        pattern = r"CREATE TABLE\s+(?P<table>\w+)\s*\((?P<columns>.+?)\)\s*;"
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


while True:
    query = input("Enter a SQL query (or 'exit' to quit): ")
    if query.lower() == "exit":
        break

    result = check_syntax(query)
    print(result)