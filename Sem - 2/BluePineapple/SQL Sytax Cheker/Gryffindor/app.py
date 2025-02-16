from flask import Flask, request, jsonify
from flask_cors import CORS
import re
app = Flask(__name__)

CORS(app)

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
        """Parses and validates SELECT statements with support for complex clauses, set operations, and proper operator handling."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # case-insensitive handling
        query = self.query.upper()
        original_query = self.query  

        
        set_ops = re.compile(r"\s+(UNION|INTERSECT)\s+", re.IGNORECASE)
        if set_ops.search(query):
            parts = set_ops.split(original_query)
            if len(parts) < 3 or not all(parts[i].upper().startswith("SELECT") for i in [0, 2]):
                return "Syntax Error: Invalid set operation structure!"
            
            for subq in [parts[0], parts[2]]:
                if "FROM" not in subq.upper():
                    return "Syntax Error: Missing FROM in set operation subquery!"

        
        pattern = re.compile(
            r"(?i)SELECT\s+(?P<select>.+?)\s+"
            r"FROM\s+(?P<from>\w+(?:\.\w+)?(?:,\s*\w+(?:\.\w+)?)*)"
            r"(?:\s+WHERE\s+(?P<where>.+?))?"
            r"(?:\s+GROUP\s+BY\s+(?P<group_by>.+?))?"
            r"(?:\s+HAVING\s+(?P<having>.+?))?"
            r"(?:\s+ORDER\s+BY\s+(?P<order_by>.+?))?"
            r"\s*;\s*$"
        , re.DOTALL)

        match = pattern.search(original_query + " ") 
        if not match:
            return "Syntax Error: Invalid SELECT statement structure!"

        clauses = match.groupdict()
        
        # Validate core clauses
        if not all([clauses['select'], clauses['from']]):
            return "Syntax Error: SELECT and FROM clauses are mandatory!"

        # Enhanced SELECT validation
        select_columns = [col.strip() for col in clauses['select'].split(",")]
        wildcard_count = sum(1 for col in select_columns if col == "*")
        if wildcard_count > 1:
            return "Syntax Error: Multiple wildcards (*) in SELECT list!"
        if any(not col for col in select_columns):
            return "Syntax Error: Empty column specification in SELECT!"

        # Table name validation
        tables = [t.strip() for t in clauses['from'].split(",")]
        for table in tables:
            if table.upper() in SQL_KEYWORDS:
                return f"Syntax Error: '{table}' is a reserved keyword!"
            if not re.match(r"^[\w\.]+$", table):
                return f"Syntax Error: Invalid table name '{table}'!"

        # Advanced WHERE clause parsing
        if clauses['where']:
            condition_pattern = re.compile(r"""
                (\w+|"[^"]+"|'[^']+')              # Column name or literal
                \s*(
                    =|!=|<>|<|>|<=|>=|LIKE|IN|NOT\s+IN
                )\s*                                # Operators
                (
                    \d+|'\w+'|"\w+"|               # Literal values
                    \((?:[^\)]+)\)                  # Value lists
                )
            """, re.IGNORECASE | re.VERBOSE)
            
            for condition in re.split(r"\s+(?:AND|OR)\s+", clauses['where']):
                if not condition_pattern.match(condition):
                    return f"Syntax Error: Invalid condition '{condition}'!"

        # GROUP BY validation
        if clauses['group_by']:
            group_cols = [col.strip() for col in clauses['group_by'].split(",")]
            invalid1 = [col for col in group_cols if col not in select_columns and col != "*"]
            invalid2 = [col for col in group_cols if col not in select_columns and col == "*"]
            # print(invalid)
            
            if invalid1 or invalid2 :
                return f"Syntax Error: GROUP BY column(s) {invalid1} {invalid2} not in SELECT list!"

        # ORDER BY validation with expression support
        if clauses['order_by']:
            order_pattern = re.compile(r"""
                ^([\w\.]+|"\w+"|'\w+')             # Column or expression
                (?:\s+(ASC|DESC))?                  # Optional direction
            $""", re.IGNORECASE | re.VERBOSE)
            
            for entry in clauses['order_by'].split(","):
                if not order_pattern.match(entry.strip()):
                    return f"Syntax Error: Invalid ORDER BY entry '{entry}'!"

        return "Valid SELECT syntax!"
   
    def parse_insert(self):
        """Parses an INSERT statement and validates syntax."""
        
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        #duplicate nokal
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
        """Validates UPDATE statements with comprehensive checks for SQL syntax."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with a semicolon (;)"

        pattern = re.compile(r"""
            ^UPDATE\s+
            (?P<table>\w+(?:\.\w+)?)                    # Table name
            \s+SET\s+
            (?P<set_clause>.+?)                         # SET clause
            (?:\s+WHERE\s+(?P<where_clause>.+?))?       # WHERE clause
            \s*;\s*$                                    # Termination
        """, re.IGNORECASE | re.VERBOSE | re.DOTALL)

        if not (match := pattern.match(self.query)):
            return "Syntax Error: Invalid UPDATE structure"

        clauses = match.groupdict()
        table_name = clauses["table"].split('.')[-1]

        if table_name.upper() in SQL_KEYWORDS:
            return f"Syntax Error: '{table_name}' is a reserved keyword"

        # SET clause validation (unchanged from previous version)

        # Enhanced WHERE clause validation
        if clauses["where_clause"]:
            where_clause = clauses["where_clause"].strip()
            conditions = re.split(r"\s+(?:AND|OR)\s+", where_clause)
            
            for condition in conditions:
                condition = condition.strip()
                
                # Handle IS NULL/IS NOT NULL explicitly
                if re.fullmatch(r"""
                    ^\w+\s+IS\s+(NOT\s+)?NULL$
                """, condition, re.IGNORECASE | re.VERBOSE):
                    continue
                    
                # Handle other conditions
                if not re.fullmatch(r"""
                    ^\w+\s*                             # Column
                    (=|!=|<|>|<=|>=|LIKE|IN|BETWEEN)    # Operator
                    \s*                                 # Whitespace
                    (?:                                 # Values:
                    '(?:[^']|'')*' |                  # Quoted strings
                    \d+(?:\.\d+)? |                   # Numbers
                    \(.+\)                            # Lists/subqueries
                    )$
                """, condition, re.IGNORECASE | re.VERBOSE):
                    return f"Syntax Error: Invalid condition '{condition}'"

        return "Valid UPDATE syntax"


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
        
        if table_name in SQL_KEYWORDS:
            return f"Syntax Error: '{table_name}' is a reserved SQL keyword and cannot be used as a table name!", None
        
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
        # print(column_list)
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
        """Parses and validates ALTER TABLE statements with detailed error messages."""
        # Initial validation
        if not self.query.endswith(';'):
            return "Syntax Error: Missing semicolon (;) at end. Did you forget to add ';'?"

        # Enhanced regex pattern
        pattern = re.compile(
            r"(?i)^ALTER\s+TABLE\s+"
            r"(?P<table>\w+)\s+"
            r"(?P<action>ADD|MODIFY|DROP)\s+"
            r"(?:(COLUMN\s+)?)"
            r"(?P<column>\w+)\s*"
            r"(?P<type>(?:INT|VARCHAR|CHAR|DECIMAL|FLOAT|BOOLEAN|DATE|TEXT)(?:\(\d+(?:,\d+)?\))?)?"
            r"(?:\s+(?P<constraints>.*?))?\s*;?$"
        )

        match = pattern.search(self.query)
        if not match:
            return ("Syntax Error: Invalid ALTER TABLE format. Common issues:\n"
                    "- Missing ADD/MODIFY/DROP keyword\n"
                    "- Incorrect column or table name format\n"
                    "- Missing column data type for ADD/MODIFY\n"
                    "Valid format: ALTER TABLE <table> <ADD|MODIFY|DROP> <column> [type] [constraints];")

        groups = match.groupdict()
        table_name = groups['table'].upper()
        action = groups['action'].upper()
        column_name = groups['column'].upper()
        data_type = (groups['type'] or '').upper()
        constraints = (groups['constraints'] or '').upper()

        # Validate names against SQL keywords
        for name, type_ in [(table_name, 'Table'), (column_name, 'Column')]:
            if name in SQL_KEYWORDS:
                return (f"{type_} Error: '{name}' is a reserved SQL keyword.\n"
                        "Solution: Use a non-reserved name or check for typos.")

        # Data type validation
        type_pattern = re.match(r"^(\w+)(?:\((\d+(?:,\d+)?)\))?$", data_type)
        base_type = type_pattern.group(1) if type_pattern else None
        size = type_pattern.group(2) if type_pattern else None
        valid_types = {"INT", "VARCHAR", "CHAR", "DECIMAL", "FLOAT", "BOOLEAN", "DATE", "TEXT"}

        if action != 'DROP' and not base_type:
            return ("Data Type Error: Missing column data type.\n"
                    "Example: ALTER TABLE table_name ADD column_name VARCHAR(255)")

        if base_type and base_type not in valid_types:
            return (f"Data Type Error: Invalid type '{base_type}'.\n"
                    f"Valid types: {', '.join(sorted(valid_types))}\n"
                    "Check for typos (e.g., 'VARCHAR' not 'VARCHR')")

        # Size validation
        size_required = {'VARCHAR', 'CHAR', 'DECIMAL'}
        size_disallowed = {'INT', 'BOOLEAN', 'DATE', 'TEXT'}
        
        if base_type in size_required and not size:
            return (f"Size Error: {base_type} requires size specification.\n"
                    f"Example: {base_type}(255) or {base_type}(10,2) for DECIMAL")
                    
        if base_type in size_disallowed and size:
            return (f"Size Error: {base_type} cannot have size specification.\n"
                    f"Remove parentheses: {base_type} instead of {base_type}(...)")

        # Constraint validation
        valid_constraints = {'PRIMARY KEY', 'NOT NULL', 'UNIQUE', 'DEFAULT'}
        if constraints:
            found_constraints = set(re.split(r'\s+', constraints.strip()))
            invalid = found_constraints - valid_constraints
            
            if invalid:
                return (f"Constraint Error: Invalid constraint(s) {', '.join(invalid)}.\n"
                        f"Allowed constraints: {', '.join(sorted(valid_constraints))}")

            if 'PRIMARY KEY' in found_constraints and action == 'MODIFY':
                return ("Constraint Error: Can't add PRIMARY KEY with MODIFY.\n"
                        "Solution: Use ADD instead or add PRIMARY KEY separately")

        # Operation-specific validation
        if action == 'ADD' and not data_type:
            return ("Operation Error: ADD requires data type specification.\n"
                    "Format: ALTER TABLE <table> ADD <column> <type> [constraints]")

        if action == 'DROP' and data_type:
            return ("Operation Error: DROP shouldn't specify data type.\n"
                    "Correct format: ALTER TABLE <table> DROP <column>")

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
        """Parses and validates a TRUNCATE TABLE statement with detailed error handling."""
        # Check for terminating semicolon
        if not self.query.endswith(";"):
            return ("Syntax Error: Missing semicolon at end of statement.\n"
                    "→ Did you forget to add ';' at the end?")

        # Case-insensitive pattern with flexible spacing
        pattern = re.compile(
            r"^\s*TRUNCATE\s+TABLE\s+(?P<table>\w+)\s*;\s*$",
            re.IGNORECASE
        )
        match = pattern.match(self.query)

        if not match:
            # Check for common TRUNCATE mistakes
            alt_match = re.match(
                r"^\s*TRUNCATE\s+(?!TABLE)(?P<table>\w+)\s*;\s*$",
                self.query,
                re.IGNORECASE
            )
            if alt_match:
                return ("Syntax Error: Missing TABLE keyword.\n"
                        "→ Did you mean: TRUNCATE TABLE {}; ?".format(alt_match.group("table")))
            
            return ("Syntax Error: Invalid TRUNCATE format.\n"
                    "→ Valid format: TRUNCATE TABLE table_name;")

        table = match.group("table").upper()

        # Validate table name
        if table in SQL_KEYWORDS:
            return ("Reserved Keyword Error: '{}' is an SQL reserved word.\n"
                    "→ Choose a different table name (e.g., 'customers' instead of 'CUSTOMER')"
                    .format(table))

        # Validate table name format
        if not re.match(r"^[A-Za-z_]\w*$", table):
            return ("Invalid Table Name: '{}'.\n"
                    "→ Table names must:\n"
                    "  - Start with a letter or underscore\n"
                    "  - Contain only letters, numbers, and underscores"
                    .format(table))

        self.valid = True
        return "Valid TRUNCATE TABLE syntax!"


    def parse(self):
        """Determine SQL statement type and validate it"""
        try:
            if not self.query:
                return {"valid": False, "message": "Empty query provided"}

            first_word = self.query.split()[0]
            parsers = {
                'SELECT': self.parse_select,
                'INSERT': self.parse_insert,
                'UPDATE': self.parse_update,
                'DELETE': self.parse_delete,
                'CREATE': self.parse_create,
                'ALTER': self.parse_alter,
                'DROP': self.parse_drop,
                'TRUNCATE': self.parse_truncate
            }
            
            if first_word not in parsers:
                return {"valid": False, "message": "Unsupported SQL statement type"}
            
            result = parsers[first_word]()
            return {"valid": "error" not in result.lower(), "message": result}
            
        except Exception as e:
            return {"valid": False, "message": f"Validation error: {str(e)}"}

def check_syntax(query):
        try:
            parser = SQLParser(query)
            return parser.parse()
        except Exception as e:
            return f"Error: {str(e)}"

@app.route('/', methods=['POST'])
def validate_sql():
    try:
        data = request.get_json()
        # print(data)
        if not data or 'query' not in data:
            return jsonify({"valid": False, "message": "No query provided"}), 400
        
        query = data['query'].strip()
        if not query:
            return jsonify({"valid": False, "message": "Empty query provided"}), 400
        
        parser = SQLParser(query)
        result = parser.parse()
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "valid": False,
            "message": f"Server error: {str(e)}"
        }), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)