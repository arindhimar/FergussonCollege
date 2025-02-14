import re

SQL_KEYWORDS = {
    "SELECT", "FROM", "WHERE", "TABLE", "CREATE", "DROP", "ALTER", "INSERT", "UPDATE", "DELETE",
    "INTO", "VALUES", "SET", "JOIN", "ORDER", "BY", "GROUP", "HAVING", "DISTINCT", "AND", "OR",
    "NOT", "IN", "BETWEEN", "LIKE", "AS", "PRIMARY", "KEY", "FOREIGN", "NULL", "DEFAULT",
    "CHECK", "INDEX", "REFERENCES", "INT", "VARCHAR", "TEXT", "DECIMAL", "FLOAT", "BOOLEAN",
    "DATE", "CHAR", "DOUBLE", "PRECISION", "UNIQUE", "AUTO_INCREMENT", "ON", "CASCADE", "RESTRICT",
    "ADD", "MODIFY", "COLUMN", "IF", "EXISTS", "TRUNCATE", "VIEW", "DATABASE", "USE", "SHOW",
    "DATABASES", "INDEXES", "CONSTRAINT", "ALL", "USERS", "PRIVILEGES", "GRANT", "REVOKE", "TO",
    "IDENTIFIED", "BY", "WITH", "OPTION", "CURRENT_TIMESTAMP", "CURRENT_DATE", "CURRENT_TIME",
    "NOW", "DATE_ADD", "DATE_SUB", "INTERVAL", "YEAR", "MONTH", "DAY", "HOUR", "MINUTE", "SECOND",
    "CASE", "WHEN", "THEN", "ELSE", "END", "JOIN", "INNER", "LEFT", "RIGHT", "OUTER", "CROSS",
    "NATURAL", "USING", "DATABASE", "SHOW", "TABLES", "SHOW", "COLUMNS", "SHOW", "INDEXES",
    "SHOW", "GRANTS", "SHOW", "PRIVILEGES", "SHOW", "PROCESSLIST", "SHOW", "STATUS"
}

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

        print("Match:", match)  
        
        if not match:
            return "Syntax Error: Invalid SELECT statement structure!"

        clauses = match.groupdict()

        # Validate SELECT & FROM
        if not clauses["select"] or not clauses["from"]:
            return "Syntax Error: SELECT and FROM are required!"
        
        if clauses["select"].strip() == ",":
            return "Syntax Error: No columns selected after SELECT!"

        # Validate WHERE clause (BETWEEN, IN, NOT IN, LIKE)
        if clauses["where"]:
            between_match = re.search(
                r"(\w+)\s+BETWEEN\s+(['\"]?[\w\s]+['\"]?)\s+AND\s+(['\"]?[\w\s]+['\"]?)",
                where_clause
            )

            if between_match:
                column, val1, val2 = between_match.groups()

                # Remove surrounding quotes
                val1_clean = val1.strip("'\"")
                val2_clean = val2.strip("'\"")

                # Check if both are numbers **even if enclosed in quotes**
                is_val1_numeric = re.match(r"^-?\d+(\.\d+)?$", val1_clean) is not None
                is_val2_numeric = re.match(r"^-?\d+(\.\d+)?$", val2_clean) is not None

                # Check if both are actual text (non-numeric)
                is_val1_text = not is_val1_numeric  # If it's not numeric, it's text
                is_val2_text = not is_val2_numeric

                print(f"BETWEEN Validation: {val1} ({'Numeric' if is_val1_numeric else 'Text'}), {val2} ({'Numeric' if is_val2_numeric else 'Text'})")

                # ✅ Ensure both values are either numbers OR both are text
                if (is_val1_numeric and is_val2_numeric) or (is_val1_text and is_val2_text):
                    return True
                else:
                    return f"Syntax Error: BETWEEN values `{val1}` and `{val2}` must be of the same type (either both numbers or both text)."


                #  Remove the matched BETWEEN condition from WHERE
                clauses["where"] = re.sub(
                    r"\w+\s+BETWEEN\s+['\"]?[\w\s]+['\"]?\s+AND\s+['\"]?[\w\s]+['\"]?", "", clauses["where"]
                ).strip()

            # #  Now split WHERE conditions (without affecting BETWEEN)
            # conditions = re.split(r"\s+AND\s+|\s+OR\s+", clauses["where"]) if clauses["where"] else []
            
            # for condition in conditions:
            #     condition = condition.strip()
            #     print("Checking condition:", condition)
            
            conditions = re.split(r"\s+AND\s+|\s+OR\s+", clauses["where"]) if clauses["where"] else []
            for condition in conditions:
                condition = condition.strip()
                print("Checking condition:", condition)

                # Ensure condition follows the pattern: column operator value
                condition_match = re.match(r"(\w+)\s*(=|!=|<|>|<=|>=|LIKE|BETWEEN|IN|NOT IN)\s*(.+)", condition, re.IGNORECASE)
                if not condition_match:
                    return f"Syntax Error: Invalid condition `{condition}` in WHERE clause! Expected format: `column operator value`."


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

                        print("Checking condition 2:", condition)
                        
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
        """Parses an INSERT statement and validates syntax."""

        self.query = self.query.strip()  # Ensure no leading/trailing spaces
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Correct regex to avoid duplicate INTO and ensure proper format
        pattern = r"^INSERT\s+INTO\s+(\w+)\s*(?:\(([^)]+)\))?\s+VALUES\s*\(([^)]+)\)\s*;$"
        match = re.match(pattern, self.query, re.IGNORECASE)

        if not match:
            return "Syntax Error: Invalid INSERT statement!"

        table, columns, values = match.groups()
        
        if table in SQL_KEYWORDS:
            return f"Syntax Error: `{table}` is a reserved SQL keyword and cannot be used as a table name!"

        # Ensure table name is present
        if not table:
            return "Syntax Error: Missing table name in INSERT INTO statement!"

        # Split columns and values properly
        column_list = [col.strip() for col in columns.split(",")] if columns else []
        value_list = [val.strip() for val in values.split(",")]

        # Ensure column count matches value count
        if column_list and len(column_list) != len(value_list):
            return f"Syntax Error: Expected {len(column_list)} values, but found {len(value_list)}!"

        # Validate values (numbers should not be in quotes, strings should be quoted)
        for val in value_list:
            if re.match(r"^\d+$", val):  # Integer check
                continue  # Valid number
            elif re.match(r"^'.*'$", val):  # Ensure string values are enclosed in single quotes
                continue  # Valid string
            else:
                return f"Syntax Error: Invalid value format `{val}`! Strings must be in single quotes."

        return "Valid INSERT syntax!"

    def parse_update(self):
        """Parses an UPDATE statement, ensuring correct structure for SET and WHERE clauses."""
        
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Match UPDATE structure
        pattern = re.compile(r"""
            ^UPDATE\s+(?P<table>\w+)\s+            # UPDATE table_name
            SET\s+(?P<set_clause>.+?)              # SET column=value assignments
            (?:\s+WHERE\s+(?P<where_clause>.+?))?  # Optional WHERE condition
            \s*;$                                  # Ensure query ends with semicolon
        """, re.IGNORECASE | re.VERBOSE)

        match = pattern.match(self.query)
        if not match:
            return "Syntax Error: Invalid UPDATE statement!"

        clauses = match.groupdict()
        table_name = clauses["table"]
        
        if table_name in SQL_KEYWORDS:
            return f"Syntax Error: `{table_name}` is a reserved SQL keyword and cannot be used as a table name!"
        
        set_clause = clauses["set_clause"].strip()
        
        
        
        where_clause = clauses["where_clause"].strip() if clauses["where_clause"] else None

        # Validate SET clause
        set_assignments = set_clause.split(",")
        for assignment in set_assignments:
            assignment = assignment.strip()

            if not re.match(r"""
                ^\w+\s*=\s*                           # column =
                (?:'.*?'|\d+|NULL|                    # 'string', number, NULL
                \w+\s*[\+\-\*/]\s*\d+|\w+\s*[\+\-\*/]\s*\w+)$ # col = col + val, col = col * col
            """, assignment, re.IGNORECASE | re.VERBOSE):
                return f"Syntax Error: Invalid assignment `{assignment}` in SET clause! Expected format: `column = value`."

        # Validate WHERE clause (if exists)
        if where_clause:
            conditions = re.split(r"\s+(AND|OR)\s+", where_clause)
            for condition in conditions:
                condition = condition.strip()

                if condition.upper() in ("AND", "OR"):
                    continue  # Skip AND/OR operators

                # Allow `IS NULL` and `IS NOT NULL`
                if re.match(r"^\w+\s+IS\s+(NULL|NOT NULL)$", condition, re.IGNORECASE):
                    continue  # Valid IS NULL / IS NOT NULL condition
                print("Checking condition: new", condition)
                if not re.match(r"""
                    ^\w+\s*                           # column
                    (?:=|!=|<|>|<=|>=|LIKE|IN|BETWEEN)\s*
                    (?:'.*?'|\d+|\(\s*\d+(?:,\s*\d+)*\s*\)|\w+\s+AND\s+\w+)?$  # Values, IN lists, and BETWEEN
                """, condition, re.IGNORECASE | re.VERBOSE):
                    return f"Syntax Error: Invalid condition `{condition}` in WHERE clause! Expected format: `column operator value`."

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
        
        

        if clauses['table'] in SQL_KEYWORDS:
            return f"Syntax Error: `{clauses['table']}` is a reserved SQL keyword and cannot be used as a table name!"
        if not clauses["table"]:
            return "Syntax Error: Missing table name after 'FROM' in DELETE statement!"

        # Ensure WHERE clause is valid
        if clauses["where"]:
            if "=" not in clauses["where"]:
                return f"Syntax Error: Invalid condition in WHERE clause: `{clauses['where']}` (Expected: column = value)"

        self.valid = True
        return "Valid DELETE syntax!"


    
    # def parse_create(self):
        # """Parses a CREATE TABLE statement."""
        # if not self.query.endswith(";"):
        #     return "Syntax Error: Query must end with ';'!"

        # pattern = r"CREATE TABLE\s+(?P<table>\w+)\s*\((?P<columns>.+?)\)\s*;"
        # match = re.match(pattern, self.query)

        # if not match:
        #     return "Syntax Error: Invalid CREATE TABLE statement!"

        # self.valid = True
        # return "Valid CREATE TABLE syntax!"

    def extract_columns(self, query):
        """Extracts columns from a CREATE TABLE statement and validates syntax."""
        match = re.match(r"CREATE TABLE\s+(\w+)\s*\((.+)\)\s*;", query, re.IGNORECASE)
        if not match:
            return "Syntax Error: Invalid CREATE TABLE statement!", None

        table_name = match.group(1)
        columns_def = match.group(2).strip()

        #printing last coloumn
        # print("Last Column:", columns_def[len(columns_def)-1])
        
        if columns_def[len(columns_def)-1] == ',':
            return "Syntax Error: Trailing comma in column definitions!", None
          
        #  **Fix: Detect trailing comma before `)`**
        if re.search(r",\s*\)$", query, re.IGNORECASE):
            return "Syntax Error: Trailing comma in column definitions!", None

        #  **Fix: Extract columns correctly, preserving `VARCHAR(30)`, `DECIMAL(10,2)`**
        column_list = []
        current_col = ""
        open_paren = 0  # Track parentheses depth

        for char in columns_def:
            if char == "," and open_paren == 0:
                column_list.append(current_col.strip())
                current_col = ""
            else:
                current_col += char
                if char == "(":
                    open_paren += 1
                elif char == ")":
                    open_paren -= 1

        if current_col.strip():
            column_list.append(current_col.strip())

        if not column_list:
            return "Syntax Error: No valid column definitions found!", None

        return "Valid column extraction!", column_list

    def validate_column_types(self, columns):
        """Validates column names, data types, and ensures proper constraints."""
        valid_data_types = {"INT", "VARCHAR", "TEXT", "DECIMAL", "FLOAT", "BOOLEAN", "DATE", "CHAR"}
        primary_key_defined = False

        for col in columns:
            parts = re.split(r"\s+", col, maxsplit=2)  # Preserve `VARCHAR(255)`

            if len(parts) < 2:
                return f"Syntax Error: Column `{col}` is missing a data type!"

            column_name = parts[0].upper()
            data_type = parts[1].upper()

            #  Ensure the column name is NOT a SQL keyword
            if column_name in SQL_KEYWORDS:
                return f"Syntax Error: `{column_name}` is a reserved SQL keyword and cannot be used as a column name!"

            #  **Fix: Detect invalid `VARCHAR` without parentheses**
            if data_type == "VARCHAR":
                return f"Syntax Error: `{column_name} {data_type}` is incorrect! Use `VARCHAR(n)` with parentheses."

            if "(" in data_type:  # Handle `DECIMAL(10,2)` or similar
                data_type_match = re.match(r"(\w+)\(\d+(?:,\d+)?\)", data_type)
                if data_type_match:
                    data_type = data_type_match.group(1)

            if data_type not in valid_data_types:
                return f"Syntax Error: Invalid data type `{data_type}` in `{col}`!"

            if re.search(r"\bPRIMARY\s+KEY\b", col, re.IGNORECASE):  # Improved PRIMARY KEY detection
                if primary_key_defined:
                    return "Syntax Error: Multiple PRIMARY KEY constraints found!"
                primary_key_defined = True

        return "Valid CREATE TABLE syntax!"

    def parse_create(self):
        """Parses a CREATE TABLE statement and validates columns."""
        result = self.extract_columns(self.query)

        # Ensure we always unpack two values
        if isinstance(result, str):  # If it returned an error message
            return result  # Directly return the error

        column_check, columns = result  # Properly unpack values

        if column_check != "Valid column extraction!":
            return column_check  # Return error if columns are invalid

        return self.validate_column_types(columns)  # Validate extracted columns

    def parse_alter(self):
        """Parses and validates an ALTER TABLE statement."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        match = re.match(
            r"ALTER TABLE\s+(\w+)\s+(ADD|MODIFY)\s+(\w+)\s+(\w+)"
            r"(\(\d+(?:,\d+)?\))?"  # Support for (size) and (precision, scale)
            r"(\s*(?:PRIMARY KEY|NOT NULL|UNIQUE)*)?\s*;",
            self.query,
            re.IGNORECASE
        )

        if not match:
            return "Syntax Error: Invalid ALTER TABLE statement! Expected: ALTER TABLE <table> ADD/MODIFY <column> <type>;"

        table_name, action, column_name, data_type, size, constraints = match.groups()
        valid_data_types = {"INT", "VARCHAR", "TEXT", "DECIMAL", "FLOAT", "BOOLEAN", "DATE", "CHAR"}

        if data_type.upper() not in valid_data_types:
            return f"Syntax Error: Invalid data type {data_type} in ALTER TABLE statement!"

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