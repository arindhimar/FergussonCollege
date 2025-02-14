def parse_delete(self):
        """Parses a DELETE statement, ensuring correct syntax, parentheses tracking, and proper IN clause validation."""
        
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = re.compile(r"""
            ^DELETE\s+FROM\s+(?P<table>\w+)\s*            # DELETE FROM table_name
            (?:WHERE\s+(?P<where>.+))?                    # Optional WHERE clause
            \s*;$                                         # Ensure query ends with a semicolon
        """, re.VERBOSE | re.IGNORECASE)

        match = pattern.match(self.query)
        if not match:
            return "Syntax Error: Invalid DELETE statement!"

        clauses = match.groupdict()
        table_name = clauses["table"]
        where_clause = clauses["where"]

        # ✅ Ensure the table name is valid
        if table_name.upper() in SQL_KEYWORDS:
            return f"Syntax Error: `{table_name}` is a reserved SQL keyword and cannot be used as a table name!"

        # ✅ Validate WHERE clause (if present)
        if where_clause:
            conditions = re.split(r"\s+AND\s+|\s+OR\s+", where_clause.strip())
            for condition in conditions:
                condition = condition.strip()

                # Ensure condition follows the pattern: column operator value
                if not re.match(r"^\w+\s*(=|!=|<|>|<=|>=|LIKE|IN|NOT IN)\s*.+$", condition, re.IGNORECASE):
                    return f"Syntax Error: Invalid condition `{condition}` in WHERE clause! Expected format: `column operator value`."

                # ✅ Ensure column name is valid
                column_name = condition.split()[0]
                if column_name.upper() in SQL_KEYWORDS:
                    return f"Syntax Error: `{column_name}` is a reserved SQL keyword and cannot be used as a column name!"
                
                                
                if " IN " in condition or " NOT IN " in condition:
                    in_match = re.match(r"(\w+)\s+(NOT IN|IN)\s*\((.+)\)", condition, re.IGNORECASE)
                    if in_match:
                        column, operator, values = in_match.groups()

                        # ✅ Track Parentheses Balance
                        open_parens = values.count("(")
                        close_parens = values.count(")")
                        print("Open Parens:", open_parens, "Close Parens:", close_parens)
                        if open_parens != close_parens:
                            return "Syntax Error: Mismatched parentheses in IN clause!"

                        # ✅ Ensure values inside IN () are properly formatted
                        values_list = re.findall(r"'[^']*'|\d+(\.\d+)?", values)  # Capture quoted strings or numbers
                        if not values_list:
                            return f"Syntax Error: Invalid {operator} values! Expected numbers or quoted strings."

        return "Valid DELETE syntax!"
    