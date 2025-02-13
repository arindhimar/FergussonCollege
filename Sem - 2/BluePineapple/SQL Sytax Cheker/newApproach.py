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

        # Support for UNION & INTERSECT
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

        # Validate SELECT & FROM
        if not clauses["select"] or not clauses["from"]:
            return "Syntax Error: SELECT and FROM are required!"

        # Validate WHERE clause (BETWEEN, IN, NOT IN, LIKE)
        if clauses["where"]:
            #  Match full BETWEEN condition first
            between_match = re.search(
                r"(\w+)\s+BETWEEN\s+(['\"]?[\w\s]+['\"]?)\s+AND\s+(['\"]?[\w\s]+['\"]?)", 
                clauses["where"]
            )

            if between_match:
                column, val1, val2 = between_match.groups()
                print("Matched BETWEEN:", column, val1, val2)  # Debug print

                #  Remove surrounding quotes for validation
                val1_clean = val1.strip("'\"")
                val2_clean = val2.strip("'\"")

                #  Check if both values are **numbers**
                is_val1_numeric = val1_clean.replace(".", "", 1).isdigit()
                is_val2_numeric = val2_clean.replace(".", "", 1).isdigit()

                #  Check if both values are **strings** (non-numeric literals)
                is_val1_text = bool(re.match(r"^[A-Za-z\s]+$", val1_clean))
                is_val2_text = bool(re.match(r"^[A-Za-z\s]+$", val2_clean))

                #  Ensure both are either numbers **or** both are text
                if (is_val1_numeric and is_val2_numeric) or (is_val1_text and is_val2_text):
                    pass  #  Valid BETWEEN condition
                else:
                    return f"Syntax Error: BETWEEN values `{val1}` and `{val2}` must be of the same type (either both numbers or both text)."

                #  Remove the matched BETWEEN condition from WHERE
                clauses["where"] = re.sub(
                    r"\w+\s+BETWEEN\s+['\"]?[\w\s]+['\"]?\s+AND\s+['\"]?[\w\s]+['\"]?", "", clauses["where"]
                ).strip()

            #  Now split WHERE conditions (without affecting BETWEEN)
            conditions = re.split(r"\s+AND\s+|\s+OR\s+", clauses["where"]) if clauses["where"] else []
            
            for condition in conditions:
                condition = condition.strip()
                print("Checking condition:", condition)

                #  Handle IN and NOT IN
                if " IN " in condition or " NOT IN " in condition:
                    in_match = re.match(r"(\w+)\s+(NOT IN|IN)\s*\(\s*([^)]+)\s*\)", condition)
                    if in_match:
                        column, operator, values = in_match.groups()
                        values_list = [v.strip() for v in values.split(",")]
                        if not all(v.replace(".", "", 1).isdigit() or v.startswith("'") for v in values_list):
                            return f"Syntax Error: Invalid {operator} values! Expected numbers or quoted strings."

                #  Handle LIKE
                if " LIKE " in condition:
                    like_match = re.match(r"(\w+)\s+LIKE\s+'(.+)'", condition)
                    if not like_match:
                        return "Syntax Error: Invalid LIKE syntax! Expected: column LIKE 'pattern'"

                    conditions = clauses["where"].strip().split(" AND ")

                    for condition in conditions:
                        condition = condition.strip()

                        print("Checking condition:", condition)
                        if "BETWEEN" in condition:
                            between_match = re.match(
                                r"(\w+)\s+BETWEEN\s+(['\"]?\w+['\"]?)\s+AND\s+(['\"]?\w+['\"]?)$", 
                                condition
                            )
                            print("Between match:", between_match)
                            if between_match:
                                column, val1, val2 = between_match.groups()
                                print("Matched BETWEEN:", column, val1, val2)

                                # Remove quotes and check if both are numbers
                                val1_clean = val1.replace("'", "").replace('"', "")
                                val2_clean = val2.replace("'", "").replace('"', "")

                                if not (val1_clean.replace(".", "", 1).isdigit() and val2_clean.replace(".", "", 1).isdigit()):
                                    return f"Syntax Error: Invalid BETWEEN values! `{val1}` and `{val2}` must be numbers."
                                continue
                            else:
                                return "Syntax Error: Invalid BETWEEN syntax! Expected: column BETWEEN value1 AND value2"

                        #  Now handle IN, NOT IN, LIKE, etc.
                        if " IN " in condition or " NOT IN " in condition:
                            in_match = re.match(r"(\w+)\s+(NOT IN|IN)\s*\(\s*([^)]+)\s*\)", condition)
                            if in_match:
                                column, operator, values = in_match.groups()
                                values_list = [v.strip() for v in values.split(",")]
                                if not all(v.replace(".", "", 1).isdigit() or v.startswith("'") for v in values_list):
                                    return f"Syntax Error: Invalid {operator} values! Expected numbers or quoted strings."

                        #  LIKE validation
                        if " LIKE " in condition:
                            like_match = re.match(r"(\w+)\s+LIKE\s+'(.+)'", condition)
                            if not like_match:
                                return "Syntax Error: Invalid LIKE syntax! Expected: column LIKE 'pattern'"

        #  Validate ORDER BY
        if clauses["order_by"]:
            order_parts = clauses["order_by"].strip().split()
            if len(order_parts) > 2:
                return "Syntax Error: ORDER BY must be followed by a column and optionally ASC or DESC!"
            if len(order_parts) == 2 and order_parts[1] not in ["ASC", "DESC"]:
                return f"Syntax Error: Invalid sorting order '{order_parts[1]}'! Use ASC or DESC."

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

        # Ensure column count matches value count
        if column_list and len(column_list) != len(value_list):
            return f"Syntax Error: Expected {len(column_list)} values, but found {len(value_list)}!"

        # Validate data types (basic check: numbers should not be enclosed in quotes)
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

        pattern = re.compile(r"""
            ^UPDATE\s+(?P<table>\w+)\s+                   # UPDATE table_name
            SET\s+(?P<set>(?:\w+\s*=\s*(?:\'.*?\'|\d+)\s*,\s*)*   # SET column=value, column=value, ...
            \w+\s*=\s*(?:\'.*?\'|\d+))                    # Last column=value (no trailing comma)
            (?:\s+WHERE\s+(?P<where>(?:\w+\s*=\s*(?:\'.*?\'|\d+)\s*(?:AND\s+)?)*) )?  # Optional WHERE condition
            \s*;$                                         # Ensure query ends with a semicolon
        """, re.VERBOSE | re.IGNORECASE)

        match = pattern.match(self.query)
        if not match:
            return "Syntax Error: Invalid UPDATE statement!"

        clauses = match.groupdict()

        # Ensure WHERE clause is valid
        if clauses["where"]:
            where_conditions = [w.strip() for w in clauses["where"].split(" AND ")]
            for condition in where_conditions:
                if "=" not in condition:
                    return f"Syntax Error: Invalid condition in WHERE clause: `{condition}` (Expected: column = value)"

        self.valid = True
        return "Valid UPDATE syntax!"



    def parse_delete(self):
        """Parses a DELETE statement, ensuring FROM is present and optionally WHERE."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = re.compile(r"""
            ^DELETE\s+FROM\s+(?P<table>\w+)\s*            # DELETE FROM table_name
            (?:WHERE\s+(?P<where>\w+\s*=\s*(?:\'.*?\'|\d+)))?  # Optional WHERE clause with column=value
            \s*;$                                         # Ensure query ends with a semicolon
        """, re.VERBOSE | re.IGNORECASE)

        match = pattern.match(self.query)
        if not match:
            return "Syntax Error: Invalid DELETE statement!"

        clauses = match.groupdict()

        # Ensure WHERE clause is valid
        if clauses["where"]:
            if "=" not in clauses["where"]:
                return f"Syntax Error: Invalid condition in WHERE clause: `{clauses['where']}` (Expected: column = value)"

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