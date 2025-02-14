
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

        # ✅ **Fix: Detect trailing comma before `)`**
        if re.search(r",\s*\)$", query, re.IGNORECASE):
            return "Syntax Error: Trailing comma in column definitions!", None

        # ✅ **Fix: Extract columns correctly, preserving `VARCHAR(30)`, `DECIMAL(10,2)`**
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

            # ✅ Ensure the column name is NOT a SQL keyword
            if column_name in SQL_KEYWORDS:
                return f"Syntax Error: `{column_name}` is a reserved SQL keyword and cannot be used as a column name!"

            # ✅ **Fix: Detect invalid `VARCHAR` without parentheses**
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