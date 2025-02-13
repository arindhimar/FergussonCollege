import re

class SQLParser:
    def __init__(self, query):
        """Initialize the parser with an SQL query."""
        self.query = query.strip().upper()  # Normalize case
        self.valid = False  # Track if query is valid

    def parse_select(self):
        """Parses a SELECT statement, handling WHERE, GROUP BY, ORDER BY, UNION, INTERSECT, and operators."""

        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Handle UNION & INTERSECT
        if " UNION " in self.query or " INTERSECT " in self.query:
            sub_queries = re.split(r"\s+UNION\s+|\s+INTERSECT\s+", self.query)
            for sub_query in sub_queries:
                if not sub_query.strip().startswith("SELECT"):
                    return "Syntax Error: UNION/INTERSECT must be between valid SELECT statements!"
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
        match = re.match(pattern, self.query, re.IGNORECASE)

        if not match:
            return "Syntax Error: Invalid SELECT statement structure!"

        clauses = match.groupdict()

        if not clauses["select"] or not clauses["from"]:
            return "Syntax Error: SELECT and FROM are required!"

        # Validate WHERE clause (BETWEEN, IN, NOT IN, LIKE)
        if clauses["where"]:
            between_error = self.validate_between(clauses["where"])
            if between_error:
                return between_error

            conditions = re.split(r"\s+AND\s+|\s+OR\s+", clauses["where"])
            for condition in conditions:
                condition = condition.strip()

                # Validate IN and NOT IN
                if " IN " in condition or " NOT IN " in condition:
                    in_match = re.match(r"(\w+)\s+(NOT IN|IN)\s*\(\s*([^)]+)\s*\)", condition)
                    if in_match:
                        column, operator, values = in_match.groups()
                        values_list = [v.strip() for v in values.split(",")]
                        if not all(v.replace(".", "", 1).isdigit() or v.startswith("'") for v in values_list):
                            return f"Syntax Error: Invalid {operator} values! Expected numbers or quoted strings."

                # Validate LIKE
                if " LIKE " in condition:
                    like_match = re.match(r"(\w+)\s+LIKE\s+'(.+)'", condition)
                    if not like_match:
                        return "Syntax Error: Invalid LIKE syntax! Expected: column LIKE 'pattern'"

        self.valid = True
        return "Valid SELECT syntax!"

    def validate_between(self, where_clause):
        """Validates BETWEEN clause ensuring values are of the same type."""
        between_match = re.search(
            r"(\w+)\s+BETWEEN\s+(['\"]?[\w\s]+['\"]?)\s+AND\s+(['\"]?[\w\s]+['\"]?)", 
            where_clause
        )

        if between_match:
            column, val1, val2 = between_match.groups()
            val1_clean = val1.strip("'\"")
            val2_clean = val2.strip("'\"")

            is_val1_numeric = val1_clean.replace(".", "", 1).isdigit()
            is_val2_numeric = val2_clean.replace(".", "", 1).isdigit()
            is_val1_text = bool(re.match(r"^[A-Za-z\s]+$", val1_clean))
            is_val2_text = bool(re.match(r"^[A-Za-z\s]+$", val2_clean))

            if not ((is_val1_numeric and is_val2_numeric) or (is_val1_text and is_val2_text)):
                return f"Syntax Error: BETWEEN values `{val1}` and `{val2}` must be of the same type."

        return ""

    def parse_delete(self):
        """Parses a DELETE statement, ensuring FROM is present and WHERE clause is valid."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = re.compile(r"""
            ^DELETE\s+FROM\s+(?P<table>\w+)\s*              # DELETE FROM table_name
            (?:WHERE\s+(?P<where>.+?))?\s*;                 # Optional WHERE clause
        """, re.VERBOSE | re.IGNORECASE)

        match = pattern.match(self.query)
        if not match:
            return "Syntax Error: Invalid DELETE statement!"

        clauses = match.groupdict()

        if "WHERE" in self.query and (not clauses["where"] or "=" not in clauses["where"]):
            return "Syntax Error: DELETE must have a valid condition after WHERE."

        self.valid = True
        return "Valid DELETE syntax!"

    def parse_insert(self):
        """Parses an INSERT statement, ensuring correct structure."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"INSERT INTO\s+(?P<table>\w+)\s*(?:\((?P<columns>.+?)\))?\s+VALUES\s*\((?P<values>.+?)\)\s*;"
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
        """Parses an ALTER TABLE statement."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"ALTER TABLE\s+(?P<table>\w+)\s+(?P<action>.+?)\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid ALTER TABLE statement!"

        self.valid = True
        return "Valid ALTER TABLE syntax!"

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
        return "Syntax Error: Unsupported SQL statement!"

def check_syntax(query):
    """Function to create a parser instance and validate the query."""
    parser = SQLParser(query)
    return parser.parse()

# Interactive prompt for testing queries
while True:
    query = input("Enter a SQL query (or 'exit' to quit): ")
    if query.lower() == "exit":
        break

    result = check_syntax(query)
    print(result)
