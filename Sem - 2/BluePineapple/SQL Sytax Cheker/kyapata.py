import re
from typing import List, Tuple, Optional

SQL_KEYWORDS = {
    "SELECT", "FROM", "WHERE", "TABLE", "CREATE", "DROP", "ALTER", "INSERT", "UPDATE", "DELETE",
    "INTO", "VALUES", "SET", "JOIN", "ORDER", "BY", "GROUP", "HAVING", "DISTINCT", "AND", "OR",
    "NOT", "IN", "BETWEEN", "LIKE", "AS", "PRIMARY", "KEY", "FOREIGN", "NULL", "DEFAULT",
    "CHECK", "INDEX", "REFERENCES", "INT", "VARCHAR", "TEXT", "DECIMAL", "FLOAT", "BOOLEAN",
    "DATE", "CHAR", "TRUNCATE"
}

class SQLParser:
    def __init__(self, query: str):
        self.query = query.strip().upper()
        self.valid = False

    def parse_select(self) -> str:
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

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

        if clauses["select"].strip() == ",":
            return "Syntax Error: No columns selected after SELECT!"

        if clauses["where"]:
            where_result = self._validate_where_clause(clauses["where"])
            if where_result != "Valid":
                return where_result

        if clauses["order_by"]:
            order_result = self._validate_order_by_clause(clauses["order_by"])
            if order_result != "Valid":
                return order_result

        self.valid = True
        return "Valid SELECT syntax!"

    def _validate_where_clause(self, where_clause: str) -> str:
        conditions = re.split(r"\s+AND\s+|\s+OR\s+", where_clause)
        for condition in conditions:
            condition = condition.strip()
            if not re.match(r"(\w+)\s*(=|!=|<|>|<=|>=|LIKE|BETWEEN|IN|NOT IN)\s*(.+)", condition, re.IGNORECASE):
                return f"Syntax Error: Invalid condition `{condition}` in WHERE clause!"

            if " IN " in condition or " NOT IN " in condition:
                in_match = re.match(r"(\w+)\s+(NOT IN|IN)\s*$$\s*([^)]+)\s*$$", condition)
                if in_match:
                    values = [v.strip() for v in in_match.group(3).split(",")]
                    if not all(v.replace(".", "", 1).isdigit() or v.startswith("'") for v in values):
                        return f"Syntax Error: Invalid {in_match.group(2)} values!"

            if " LIKE " in condition:
                like_match = re.match(r"(\w+)\s+LIKE\s+'(.+)'", condition)
                if not like_match:
                    return "Syntax Error: Invalid LIKE syntax!"

            if " BETWEEN " in condition:
                between_match = re.match(r"(\w+)\s+BETWEEN\s+(['\"]?\w+['\"]?)\s+AND\s+(['\"]?\w+['\"]?)$", condition)
                if not between_match:
                    return "Syntax Error: Invalid BETWEEN syntax!"

        return "Valid"

    def _validate_order_by_clause(self, order_by_clause: str) -> str:
        order_parts = order_by_clause.strip().split()
        if len(order_parts) > 2:
            return "Syntax Error: ORDER BY must be followed by a column and optionally ASC or DESC!"
        if len(order_parts) == 2 and order_parts[1] not in ["ASC", "DESC"]:
            return f"Syntax Error: Invalid sorting order '{order_parts[1]}'! Use ASC or DESC."
        return "Valid"

    def parse_insert(self) -> str:
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"INSERT INTO\s+(?P<table>\w+)\s*(?:$$(?P<columns>.+?)$$)?\s+VALUES\s*$$(?P<values>.+?)$$\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid INSERT statement!"

        clauses = match.groupdict()
        columns = clauses["columns"]
        values = clauses["values"]

        column_list = [col.strip() for col in columns.split(",")] if columns else []
        value_list = [val.strip() for val in values.split(",")]

        if column_list and len(column_list) != len(value_list):
            return f"Syntax Error: Expected {len(column_list)} values, but found {len(value_list)}!"

        for val in value_list:
            if not re.match(r"^\d+$|^'.*'$", val):
                return f"Syntax Error: Invalid value format: {val}"

        self.valid = True
        return "Valid INSERT syntax!"

    def parse_update(self) -> str:
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = re.compile(r"""
            ^UPDATE\s+(?P<table>\w+)\s+
            SET\s+(?P<set_clause>.+?)
            (?:\s+WHERE\s+(?P<where_clause>.+?))?
            \s*;$
        """, re.IGNORECASE | re.VERBOSE)

        match = pattern.match(self.query)
        if not match:
            return "Syntax Error: Invalid UPDATE statement!"

        clauses = match.groupdict()
        set_clause = clauses["set_clause"].strip()
        where_clause = clauses["where_clause"].strip() if clauses["where_clause"] else None

        set_result = self._validate_set_clause(set_clause)
        if set_result != "Valid":
            return set_result

        if where_clause:
            where_result = self._validate_where_clause(where_clause)
            if where_result != "Valid":
                return where_result

        self.valid = True
        return "Valid UPDATE syntax!"

    def _validate_set_clause(self, set_clause: str) -> str:
        set_assignments = set_clause.split(",")
        for assignment in set_assignments:
            assignment = assignment.strip()
            if not re.match(r"""
                ^\w+\s*=\s*
                (?:'.*?'|\d+|NULL|
                \w+\s*[\+\-\*/]\s*\d+|\w+\s*[\+\-\*/]\s*\w+)$
            """, assignment, re.IGNORECASE | re.VERBOSE):
                return f"Syntax Error: Invalid assignment `{assignment}` in SET clause!"
        return "Valid"

    def parse_delete(self) -> str:
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = re.compile(r"""
            ^DELETE\s+FROM\s+(?P<table>\w+)\s*
            (?:WHERE\s+(?P<where>.+))?
            \s*;$
        """, re.VERBOSE | re.IGNORECASE)

        match = pattern.match(self.query)
        if not match:
            return "Syntax Error: Invalid DELETE statement!"

        clauses = match.groupdict()

        if clauses['table'] in SQL_KEYWORDS:
            return f"Syntax Error: `{clauses['table']}` is a reserved SQL keyword and cannot be used as a table name!"

        if clauses["where"]:
            where_result = self._validate_where_clause(clauses["where"])
            if where_result != "Valid":
                return where_result

        self.valid = True
        return "Valid DELETE syntax!"

    def parse_create(self) -> str:
        result = self._extract_columns(self.query)
        if isinstance(result, str):
            return result

        column_check, columns = result
        if column_check != "Valid column extraction!":
            return column_check

        return self._validate_column_types(columns)

    def _extract_columns(self, query: str) -> Tuple[str, Optional[List[str]]]:
        match = re.match(r"CREATE TABLE\s+(\w+)\s*$$(.+)$$\s*;", query, re.IGNORECASE)
        if not match:
            return "Syntax Error: Invalid CREATE TABLE statement!", None

        columns_def = match.group(2).strip()

        if columns_def.endswith(','):
            return "Syntax Error: Trailing comma in column definitions!", None

        if re.search(r",\s*\)$", query, re.IGNORECASE):
            return "Syntax Error: Trailing comma in column definitions!", None

        column_list = []
        current_col = ""
        open_paren = 0

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

    def _validate_column_types(self, columns: List[str]) -> str:
        valid_data_types = {"INT", "VARCHAR", "TEXT", "DECIMAL", "FLOAT", "BOOLEAN", "DATE", "CHAR"}
        primary_key_defined = False

        for col in columns:
            parts = re.split(r"\s+", col, maxsplit=2)

            if len(parts) < 2:
                return f"Syntax Error: Column `{col}` is missing a data type!"

            column_name = parts[0].upper()
            data_type = parts[1].upper()

            if column_name in SQL_KEYWORDS:
                return f"Syntax Error: `{column_name}` is a reserved SQL keyword and cannot be used as a column name!"

            if data_type == "VARCHAR":
                return f"Syntax Error: `{column_name} {data_type}` is incorrect! Use `VARCHAR(n)` with parentheses."

            if "(" in data_type:
                data_type_match = re.match(r"(\w+)$$\d+(?:,\d+)?$$", data_type)
                if data_type_match:
                    data_type = data_type_match.group(1)

            if data_type not in valid_data_types:
                return f"Syntax Error: Invalid data type `{data_type}` in `{col}`!"

            if re.search(r"\bPRIMARY\s+KEY\b", col, re.IGNORECASE):
                if primary_key_defined:
                    return "Syntax Error: Multiple PRIMARY KEY constraints found!"
                primary_key_defined = True

        return "Valid CREATE TABLE syntax!"

    def parse_alter(self) -> str:
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        match = re.match(
            r"ALTER TABLE\s+(\w+)\s+(ADD|MODIFY)\s+(\w+)\s+(\w+)"
            r"($$\d+(?:,\d+)?$$)?"
            r"(\s*(?:PRIMARY KEY|NOT NULL|UNIQUE)*)?\s*;",
            self.query,
            re.IGNORECASE
        )

        if not match:
            return "Syntax Error: Invalid ALTER TABLE statement!"

        _, _, _, data_type, _, _ = match.groups()
        valid_data_types = {"INT", "VARCHAR", "TEXT", "DECIMAL", "FLOAT", "BOOLEAN", "DATE", "CHAR"}

        if data_type.upper() not in valid_data_types:
            return f"Syntax Error: Invalid data type {data_type} in ALTER TABLE statement!"

        self.valid = True
        return "Valid ALTER TABLE syntax!"

    def parse_drop(self) -> str:
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"DROP TABLE\s+(?P<table>\w+)\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid DROP TABLE statement!"

        self.valid = True
        return "Valid DROP TABLE syntax!"

    def parse_truncate(self) -> str:
        if not self.query.endswith(";"):
            return "Syntax Error: Query must end with ';'!"

        pattern = r"TRUNCATE TABLE\s+(?P<table>\w+)\s*;"
        match = re.match(pattern, self.query)

        if not match:
            return "Syntax Error: Invalid TRUNCATE TABLE statement!"

        self.valid = True
        return "Valid TRUNCATE TABLE syntax!"

    def parse(self) -> str:
        first_word = self.query.split()[0]
        
        parse_methods = {
            "SELECT": self.parse_select,
            "INSERT": self.parse_insert,
            "UPDATE": self.parse_update,
            "DELETE": self.parse_delete,
            "CREATE": self.parse_create,
            "ALTER": self.parse_alter,
            "DROP": self.parse_drop,
            "TRUNCATE": self.parse_truncate
        }
        
        parse_method = parse_methods.get(first_word)
        if parse_method:
            return parse_method()
        return "Syntax Error: Unsupported SQL statement!"

def check_syntax(query: str) -> str:
    parser = SQLParser(query)
    return parser.parse()

# Example usage
if __name__ == "__main__":
    # test_queries = [
    #     "SELECT * FROM users WHERE age > 18;",
    #     "INSERT INTO products (name, price) VALUES ('Widget', 9.99);",
    #     "UPDATE customers SET status = 'VIP' WHERE total_purchases > 1000;",
    #     "DELETE FROM orders WHERE order_date < '2023-01-01';",
    #     "CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(50), salary DECIMAL(10,2));",
    #     "ALTER TABLE users ADD COLUMN email VARCHAR(100);",
    #     "DROP TABLE old_records;",
    #     "TRUNCATE TABLE logs;"
    # ]

    # for query in test_queries:
    #     result = check_syntax(query)
    #     print(f"Query: {query}")
        # print(f"Result: {result}\n")

# Interactive mode
    while True:
        query = input("Enter a SQL query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break

        result = check_syntax(query)
        print(result)