from flask import Flask, request, jsonify
from flask_cors import CORS
from check_syntax import SQLParser

app = Flask(__name__)
CORS(app)


import re

SQL_KEYWORDS = {
    "SELECT", "FROM", "WHERE", "TABLE", "CREATE", "DROP", "ALTER", "INSERT", "UPDATE", "DELETE",
    "INTO", "VALUES", "SET", "JOIN", "ORDER", "BY", "GROUP", "HAVING", "DISTINCT", "AND", "OR",
    "NOT", "IN", "BETWEEN", "LIKE", "AS", "PRIMARY", "KEY", "FOREIGN", "NULL", "DEFAULT",
    "CHECK", "INDEX", "REFERENCES", "INT", "VARCHAR", "TEXT", "DECIMAL", "FLOAT", "BOOLEAN",
    "DATE", "CHAR", "DOUBLE", "PRECISION", "UNIQUE", "AUTO_INCREMENT", "ON", "CASCADE", "RESTRICT",
    "ADD", "MODIFY", "COLUMN", "IF", "EXISTS", "TRUNCATE", "VIEW", "DATABASE", "USE", "SHOW",
    "DATABASES", "INDEXES", "CONSTRAINT", "ALL", "PRIVILEGES", "GRANT", "REVOKE", "TO",
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

        if not match:
            return "Syntax Error: Invalid SELECT statement structure!"

        clauses = match.groupdict()
        
        select_clause = clauses["select"].strip()


        # Validate SELECT & FROM
        if not clauses["select"] or not clauses["from"]:
            return "Syntax Error: SELECT and FROM are required!"
        
        if clauses["select"].strip() == ",":
            return "Syntax Error: No columns selected after SELECT!"

        # Validate WHERE clause (Without BETWEEN)
        if clauses["where"]:
            conditions = re.split(r"\s+AND\s+|\s+OR\s+", clauses["where"]) if clauses["where"] else []
            for condition in conditions:
                condition = condition.strip()

                # Ensure condition follows the pattern: column operator value
                condition_match = re.match(r"(\w+)\s*(=|!=|<|>|<=|>=|LIKE|IN|NOT IN)\s*(.+)", condition, re.IGNORECASE)
                if not condition_match:
                    return f"Syntax Error: Invalid condition `{condition}` in WHERE clause! Expected format: `column operator value`."

                # Handle IN and NOT IN
                if " IN " in condition or " NOT IN " in condition:
                    in_match = re.match(r"(\w+)\s+(NOT IN|IN)\s*\(\s*([^)]+)\s*\)", condition)
                    if in_match:
                        column, operator, values = in_match.groups()
                        values_list = [v.strip() for v in values.split(",")]
                        if not all(v.replace(".", "", 1).isdigit() or v.startswith("'") for v in values_list):
                            return f"Syntax Error: Invalid {operator} values! Expected numbers or quoted strings."

                # Handle LIKE
                if " LIKE " in condition:
                    like_match = re.match(r"(\w+)\s+LIKE\s+'(.+)'", condition)
                    if not like_match:
                        return "Syntax Error: Invalid LIKE syntax! Expected: column LIKE 'pattern'"

        # Validate ORDER BY
        if clauses["order_by"]:
            order_parts = clauses["order_by"].strip().split()
            if len(order_parts) > 2:
                return "Syntax Error: ORDER BY must be followed by a column and optionally ASC or DESC!"
            if len(order_parts) == 2 and order_parts[1] not in ["ASC", "DESC"]:
                return f"Syntax Error: Invalid sorting order '{order_parts[1]}'! Use ASC or DESC."

        return "Valid SELECT syntax!"

   
    def parse_insert(self):
        """Parses an INSERT statement and validates syntax."""
        
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Correct regex to avoid duplicate INTO and ensure proper format
        pattern = r"^INSERT\s+INTO\s+(\w+)\s*(?:\(([^)]+)\))?\s+VALUES\s*\((.+)\)\s*;$"
        match = re.match(pattern, self.query, re.IGNORECASE)
        
        
        
        #insert into table_name (col1, col2, col3) values (val1, val2, val3);

        if not match:
            return "Syntax Error: Invalid INSERT statement!"

        table, columns, values = match.groups()

        # Ensure table name is present
        if not table:
            return "Syntax Error: Missing table name in INSERT INTO statement!"
        
        if table in SQL_KEYWORDS:
            return f"Syntax Error: `{table}` is a reserved SQL keyword and cannot be used as a table name!"

        
        # Split columns safely
        column_list = [col.strip().upper() for col in columns.split(",")] if columns else []

        # **Fixed:** Use `_split_values_correctly` to correctly parse values
        value_list = self._split_values_correctly(values)

        print("Column List:", column_list)  # Debugging output
        print("Value List:", value_list)  # Debugging output

        # Ensure column count matches value count
        if column_list and len(column_list) != len(value_list):
            return f"Syntax Error: Expected {len(column_list)} values, but found {len(value_list)}!"

        # Validate values (numbers should not be in quotes, strings should be quoted)
        for val in value_list:
            if re.match(r"^\d+(\.\d+)?$", val):  # Integer or float check
                continue  # Valid number
            elif re.match(r"^'.*'$", val):  # Ensure string values are enclosed in single quotes
                continue  # Valid string
            else:
                return f"Syntax Error: Invalid value format `{val}`! Strings must be in single quotes."

        return "Valid INSERT syntax!"

    def _split_values_correctly(self, values):
        """
        Splits values while correctly handling commas inside quoted strings.
        Example: "1, 'Table, Chair', 299.99" -> ['1', "'Table, Chair'", '299.99']
        """
        parts = []
        current = ""
        in_quotes = False

        for char in values:
            if char == "'" and (not current or current[-1] != "\\"):  # Handle single quotes
                in_quotes = not in_quotes
            if char == "," and not in_quotes:  # Only split on commas outside quotes
                parts.append(current.strip())
                current = ""
            else:
                current += char

        if current.strip():
            parts.append(current.strip())

        return parts     


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
        """Parses a DELETE statement with comprehensive value quoting validation."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = re.compile(r"""
            ^DELETE\s+FROM\s+(?P<table>\w+)\s*
            (?:\s+WHERE\s+(?P<where>.+?))?
            \s*;$
        """, re.VERBOSE | re.IGNORECASE | re.DOTALL)

        match = pattern.match(self.query)
        if not match:
            return "Syntax Error: Invalid DELETE statement structure. Example: DELETE FROM table [WHERE condition];"

        clauses = match.groupdict()
        table_name = clauses["table"]
        where_clause = clauses["where"] or ""

        # Validate table name
        if table_name.upper() in SQL_KEYWORDS:
            return f"Syntax Error: '{table_name}' is a reserved SQL keyword!"

        if where_clause:
            conditions = re.split(r"\s+(?:AND|OR)\s+", where_clause, flags=re.IGNORECASE)
            
            for condition in conditions:
                # Check for double quotes first
                if '"' in condition:
                    return ("Syntax Error: Double quotes (\") are not allowed for string values\n"
                            "→ Use single quotes (') instead: WHERE name IN ('Alice', 'Bob')")

                # Enhanced condition validation
                if not re.match(r"""
                    (^\w+\s+(?:IS\s+(?:NOT\s+)?NULL)$) |  # NULL checks
                    (^\w+\s*                               # Column name
                    (=|!=|<|>|<=|>=|LIKE|IN)\s*            # Operator
                    (                                      # Value(s)
                        '(?:[^']|'')*'|                    # Proper quoted string
                        \d+(?:\.\d+)?|                     # Numbers
                        \((?:'[^']*'|\d+\s*,?\s*)+\)       # IN list with valid values
                    )$)
                """, condition, re.IGNORECASE | re.VERBOSE | re.X):
                    return (f"Syntax Error: Invalid condition '{condition}'\n"
                            "Valid formats:\n"
                            "- column = 'value'\n"
                            "- column IS [NOT] NULL\n"
                            "- column IN (value1, value2)(string not supported)\n"
                            "- column LIKE 'pattern%'\n"
                            )

        return "Valid DELETE syntax!"
    
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
            r"(\(\d+(?:,\d+)?\))?"  
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

        pattern = r"DROP TABLE\s+(?P<table>[\w, ]+)\s*;"  
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid DROP TABLE statement!"

        tables_string = match.group("table")
        tables = [table.strip() for table in tables_string.split(",")]  # Split by comma and strip whitespace

        if not tables:
            return "Syntax Error: Missing table name in DROP TABLE statement!"

        if any(table in SQL_KEYWORDS for table in tables):
            return "Syntax Error: SQL keywords cannot be used as table names!"

        self.valid = True
        return "Valid DROP TABLE syntax!"

    def parse_truncate(self):
        """Parses a TRUNCATE TABLE statement."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"TRUNCATE TABLE\s+(?P<table>\w+)\s*;"
        match = re.match(pattern, self.query)
        
        table = match.group("table") if match else None
        
        if table in SQL_KEYWORDS:
            return f"Syntax Error: `{table}` is a reserved SQL keyword and cannot be used as a table name!"
        
        print ("Table:", table)

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


@app.route('/', methods=['POST'])
def hello_name():
    data = request.get_json()
    print(data)
    result = check_syntax(data)
    return jsonify(result)

if __name__ == '__main__':

    app.run(debug=True)
