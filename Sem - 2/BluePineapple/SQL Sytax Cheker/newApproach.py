import re

class SQLParser:
    def __init__(self, query):
        self.query = query.strip().upper()  # Normalize case
        self.valid = False  # Track if query is valid

    def parse_select(self):
        """ Parses a SELECT statement, handling aggregate functions, WHERE, GROUP BY, ORDER BY. """
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

        clauses = match.groupdict()

        # Validate required parts
        if not clauses["select"] or not clauses["from"]:
            return "Syntax Error: SELECT and FROM are required!"

        # Ensure GROUP BY contains all non-aggregate columns
        select_columns = [col.strip() for col in clauses["select"].split(",")]
        if clauses["group_by"]:
            group_columns = [col.strip() for col in clauses["group_by"].split(",")]
            for col in select_columns:
                if not re.match(r"(COUNT|SUM|AVG|MIN|MAX)\(.*\)", col) and col not in group_columns:
                    return "Syntax Error: All non-aggregate columns must be in GROUP BY!"

        # HAVING must follow GROUP BY
        if clauses["having"] and not clauses["group_by"]:
            return "Syntax Error: 'HAVING' must be used with 'GROUP BY'!"

        self.valid = True
        return "Valid SELECT syntax!"

    def parse_insert(self):
        """ Parses an INSERT statement, ensuring correct structure. """
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Extract table and values
        pattern = r"INSERT INTO\s+(?P<table>\w+)\s*(?:\((?P<columns>.+?)\))?\s+VALUES\s*\((?P<values>.+?)\)\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid INSERT statement!"

        clauses = match.groupdict()
        if not clauses["table"] or not clauses["values"]:
            return "Syntax Error: INSERT must have table name and values!"

        # Ensure column count matches value count
        if clauses["columns"]:
            column_count = len(clauses["columns"].split(","))
            value_count = len(clauses["values"].split(","))
            if column_count != value_count:
                return f"Syntax Error: Expected {column_count} values, but found {value_count}!"

        self.valid = True
        return "Valid INSERT syntax!"

    def parse_update(self):
        """ Parses an UPDATE statement, ensuring it has SET and optionally WHERE. """
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Extract table, SET clause, and optional WHERE
        pattern = r"UPDATE\s+(?P<table>\w+)\s+SET\s+(?P<set>.+?)(?:\s+WHERE\s+(?P<where>.+?))?\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid UPDATE statement!"

        clauses = match.groupdict()
        if not clauses["table"] or not clauses["set"]:
            return "Syntax Error: UPDATE must have a table and SET clause!"

        # Ensure SET clause has valid column assignments
        set_parts = [part.strip() for part in clauses["set"].split(",")]
        for part in set_parts:
            if "=" not in part:
                return f"Syntax Error: Invalid assignment in SET clause: {part}"

        self.valid = True
        return "Valid UPDATE syntax!"

    def parse_delete(self):
        """ Parses a DELETE statement, ensuring FROM is present and optionally WHERE. """
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Extract table and optional WHERE clause
        pattern = r"DELETE FROM\s+(?P<table>\w+)(?:\s+WHERE\s+(?P<where>.+?))?\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid DELETE statement!"

        clauses = match.groupdict()
        if not clauses["table"]:
            return "Syntax Error: DELETE must specify a table!"

        self.valid = True
        return "Valid DELETE syntax!"

    def parse(self):
        """ Determines SQL statement type and validates it. """
        first_word = self.query.split()[0]
        if first_word == "SELECT":
            return self.parse_select()
        elif first_word == "INSERT":
            return self.parse_insert()
        elif first_word == "UPDATE":
            return self.parse_update()
        elif first_word == "DELETE":
            return self.parse_delete()
        return "Syntax Error: Unsupported SQL statement!"


while True:
    query = input("Enter a SQL query: ")
    if not query:
        break

    parser = SQLParser(query)
    result = parser.parse()
    print(result)
    if parser.valid:
        break
