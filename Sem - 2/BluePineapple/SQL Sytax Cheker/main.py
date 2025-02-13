import re

class SQLParser:
    def __init__(self, query):
        """Initialize the parser with an SQL query."""
        self.query = query.strip()
        self.valid = False  # Track query validity

    def parse_create(self):
        """Parses and validates a CREATE TABLE statement."""
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        # Match table name and column definitions while handling `(size,scale)` correctly
        match = re.match(r"CREATE TABLE\s+(\w+)\s*\((.+)\)\s*;", self.query, re.IGNORECASE)
        if not match:
            return "Syntax Error: Invalid CREATE TABLE statement!"

        table_name = match.group(1)
        columns_def = match.group(2)

        #  Improved regex to correctly extract column definitions while keeping `DECIMAL(10,2)` intact
        column_pattern = re.compile(
            r"\s*(\w+)\s+"                # Column name
            r"(\w+)"                      # Data type
            r"(\(\d+(?:,\d+)?\))?"         # (size) or (precision, scale)
            r"(\s*(?:PRIMARY KEY|NOT NULL|UNIQUE|DEFAULT\s+\S+|AUTO_INCREMENT)*)?\s*$",
            re.IGNORECASE
        )

        # **🔧 Fix:** Use regex to properly split columns while handling `DECIMAL(10,2)`
        columns = re.findall(r"\s*\w+\s+\w+(?:\(\d+(?:,\d+)?\))?(?:\s+(?:PRIMARY KEY|NOT NULL|UNIQUE|DEFAULT\s+\S+|AUTO_INCREMENT)*)?", columns_def)
        
        if not columns:
            return "Syntax Error: No valid column definitions found!"

        valid_data_types = {"INT", "VARCHAR", "TEXT", "DECIMAL", "FLOAT", "BOOLEAN", "DATE", "CHAR"}
        primary_key_defined = False

        for col in columns:
            col_match = column_pattern.match(col)
            if not col_match:
                return f"Syntax Error: Invalid column definition `{col}`!"

            column_name, data_type, size, constraints = col_match.groups()

            if data_type.upper() not in valid_data_types:
                return f"Syntax Error: Invalid data type `{data_type}` in `{col}`!"

            if constraints and "PRIMARY KEY" in constraints:
                if primary_key_defined:
                    return "Syntax Error: Multiple PRIMARY KEY constraints found!"
                primary_key_defined = True

        self.valid = True
        return "Valid CREATE TABLE syntax!"

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
            return "Syntax Error: Invalid ALTER TABLE statement! Expected: `ALTER TABLE <table> ADD/MODIFY <column> <type>;`"

        table_name, action, column_name, data_type, size, constraints = match.groups()
        valid_data_types = {"INT", "VARCHAR", "TEXT", "DECIMAL", "FLOAT", "BOOLEAN", "DATE", "CHAR"}

        if data_type.upper() not in valid_data_types:
            return f"Syntax Error: Invalid data type `{data_type}` in ALTER TABLE statement!"

        self.valid = True
        return "Valid ALTER TABLE syntax!"

    def parse(self):
        """Determines SQL statement type and validates it."""
        words = self.query.split()
        if not words:
            return "Syntax Error: Empty SQL statement!"

        first_word = words[0].upper()
        if first_word == "CREATE":
            return self.parse_create()
        elif first_word == "ALTER":
            return self.parse_alter()
        return "Syntax Error: Unsupported SQL statement!"

def check_syntax(query):
    """Creates a parser instance and validates the query."""
    parser = SQLParser(query)
    return parser.parse()

# Interactive CLI for testing queries
while True:
    query = input("Enter a SQL query (or 'exit' to quit): ").strip()
    if not query:
        continue  # Ignore empty inputs

    if query.lower() == "exit":
        break

    result = check_syntax(query)
    print(result)
