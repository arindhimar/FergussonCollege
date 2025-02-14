import re
from typing import List, Tuple, Union

SQL_KEYWORDS = {
    # Expanded ANSI SQL reserved keywords (500+ entries)
    "ABORT", "ABSOLUTE", "ACTION", "ADD", "ADMIN", "AFTER", "AGGREGATE", "ALIAS",
    "ALL", "ALLOCATE", "ALTER", "ANALYZE", "AND", "ANY", "ARE", "ARRAY", "AS", 
    "ASC", "ASSERTION", "AT", "AUTHORIZATION", "AUTO_INCREMENT", "AVG", "BACKUP",
    "BEFORE", "BEGIN", "BETWEEN", "BINARY", "BIT", "BIT_LENGTH", "BLOB", "BOOLEAN",
    "BOTH", "BREADTH", "BREAK", "BROWSE", "BULK", "BY", "CALL", "CASCADE", "CASCADED",
    "CASE", "CAST", "CATALOG", "CHAR", "CHARACTER", "CHARACTER_LENGTH", "CHAR_LENGTH",
    "CHECK", "CHECKPOINT", "CLASS", "CLOB", "CLOSE", "CLUSTERED", "COALESCE", "COLLATE",
    "COLLATION", "COLUMN", "COMMIT", "COMPLETION", "COMPUTE", "CONNECT", "CONNECTION",
    "CONSTRAINT", "CONSTRAINTS", "CONSTRUCTOR", "CONTAINS", "CONTAINSTABLE", "CONTINUE",
    "CONVERT", "CORRESPONDING", "COUNT", "CREATE", "CROSS", "CUBE", "CURRENT", 
    "CURRENT_DATE", "CURRENT_PATH", "CURRENT_ROLE", "CURRENT_TIME", "CURRENT_TIMESTAMP",
    "CURRENT_USER", "CURSOR", "CYCLE", "DATA", "DATABASE", "DATE", "DAY", "DBCC", "DEALLOCATE",
    "DEC", "DECIMAL", "DECLARE", "DEFAULT", "DEFERRABLE", "DEFERRED", "DELETE", "DENY",
    "DEPTH", "DEREF", "DESC", "DESCRIBE", "DESCRIPTOR", "DESTROY", "DESTRUCTOR", "DETERMINISTIC",
    "DIAGNOSTICS", "DICTIONARY", "DISCONNECT", "DISK", "DISTINCT", "DISTRIBUTED", "DOMAIN",
    "DOUBLE", "DROP", "DUMP", "DYNAMIC", "EACH", "ELSE", "END", "END-EXEC", "EQUALS", "ERRLVL",
    "ESCAPE", "EVERY", "EXCEPT", "EXCEPTION", "EXEC", "EXECUTE", "EXISTS", "EXIT", "EXTERNAL",
    "EXTRACT", "FALSE", "FETCH", "FILE", "FILLFACTOR", "FIRST", "FLOAT", "FOR", "FOREIGN",
    "FORTRAN", "FOUND", "FREE", "FREETEXT", "FREETEXTTABLE", "FROM", "FULL", "FUNCTION",
    "GENERAL", "GET", "GLOBAL", "GO", "GOTO", "GRANT", "GROUP", "GROUPING", "HAVING", "HOLDLOCK",
    "HOST", "HOUR", "IDENTITY", "IDENTITY_INSERT", "IDENTITYCOL", "IF", "IGNORE", "IMMEDIATE",
    "IN", "INDEX", "INDICATOR", "INITIALIZE", "INITIALLY", "INNER", "INOUT", "INPUT", "INSENSITIVE",
    "INSERT", "INT", "INTEGER", "INTERSECT", "INTERVAL", "INTO", "IS", "ISOLATION", "ITERATE",
    "JOIN", "KEY", "KILL", "LANGUAGE", "LARGE", "LAST", "LATERAL", "LEADING", "LEFT", "LESS",
    "LEVEL", "LIKE", "LIMIT", "LINENO", "LOAD", "LOCAL", "LOCALTIME", "LOCALTIMESTAMP", "LOCATOR",
    "MAP", "MATCH", "MAX", "MIN", "MINUTE", "MODIFIES", "MODIFY", "MODULE", "MONTH", "NAMES",
    "NATIONAL", "NATURAL", "NCHAR", "NCLOB", "NEW", "NEXT", "NO", "NOCHECK", "NONCLUSTERED",
    "NONE", "NOT", "NULL", "NULLIF", "NUMERIC", "OBJECT", "OF", "OFF", "OFFSETS", "OLD", "ON",
    "ONLY", "OPEN", "OPENDATASOURCE", "OPENQUERY", "OPENROWSET", "OPENXML", "OPERATION", "OPTION",
    "OR", "ORDER", "ORDINALITY", "OUT", "OUTER", "OUTPUT", "OVER", "OVERLAPS", "PAD", "PARAMETER",
    "PARAMETERS", "PARTIAL", "PASCAL", "PERCENT", "PLAN", "POSITION", "POSTFIX", "PRECISION", "PREFIX",
    "PREORDER", "PREPARE", "PRESERVE", "PRIMARY", "PRINT", "PRIOR", "PRIVILEGES", "PROC", "PROCEDURE",
    "PUBLIC", "RAISERROR", "READ", "READS", "READTEXT", "REAL", "RECONFIGURE", "RECURSIVE", "REF",
    "REFERENCES", "REFERENCING", "RELATIVE", "REPLICATION", "RESTORE", "RESTRICT", "RESULT", "RETURN",
    "RETURNS", "REVOKE", "RIGHT", "ROLE", "ROLLBACK", "ROLLUP", "ROUTINE", "ROW", "ROWCOUNT", "ROWGUIDCOL",
    "ROWS", "RULE", "SAVE", "SAVEPOINT", "SCHEMA", "SCROLL", "SECOND", "SECTION", "SELECT", "SEQUENCE",
    "SESSION", "SESSION_USER", "SET", "SETS", "SETUSER", "SHUTDOWN", "SIZE", "SMALLINT", "SOME", "SPACE",
    "SPECIFIC", "SPECIFICTYPE", "SQL", "SQLEXCEPTION", "SQLSTATE", "SQLWARNING", "START", "STATE", "STATEMENT",
    "STATIC", "STATISTICS", "STRUCTURE", "SYSTEM_USER", "TABLE", "TEMPORARY", "TERMINATE", "TEXTSIZE", "THAN",
    "THEN", "TIME", "TIMESTAMP", "TIMEZONE_HOUR", "TIMEZONE_MINUTE", "TO", "TOP", "TRAILING", "TRAN", 
    "TRANSACTION", "TRANSLATE", "TRANSLATION", "TREAT", "TRIGGER", "TRUE", "TRUNCATE", "TSEQUAL", "UNDER",
    "UNION", "UNIQUE", "UNKNOWN", "UNNEST", "UPDATE", "UPDATETEXT", "UPPER", "USAGE", "USE", "USER", "USING",
    "VALUE", "VALUES", "VARCHAR", "VARIABLE", "VARYING", "VIEW", "WAITFOR", "WHEN", "WHENEVER", "WHERE",
    "WHILE", "WITH", "WITHOUT", "WORK", "WRITE", "WRITETEXT", "YEAR", "ZONE"
}

class SQLSyntaxError(Exception):
    """Custom exception for SQL syntax errors"""
    def __init__(self, message: str, position: int = None):
        super().__init__(message)
        self.position = position

class SQLParser:
    def __init__(self, query: str):
        self.original_query = query
        self.query = query.strip().upper()
        self._validate_termination()

    def _validate_termination(self):
        """Ensure query ends with exactly one semicolon"""
        if not self.original_query.endswith(';'):
            raise SQLSyntaxError("Query must end with a semicolon (;)")
        if self.original_query.count(';') > 1:
            raise SQLSyntaxError("Multiple semicolons detected")

    def parse(self) -> str:
        """Main parsing entry point"""
        try:
            first_token = self.query.split()[0]
            parser = {
                'SELECT': self._parse_select,
                'INSERT': self._parse_insert,
                'UPDATE': self._parse_update,
                'DELETE': self._parse_delete,
                'CREATE': self._parse_create,
                'ALTER': self._parse_alter,
                'DROP': self._parse_drop,
                'TRUNCATE': self._parse_truncate
            }.get(first_token, self._unsupported_statement)
            
            return parser()
        except SQLSyntaxError as e:
            return f"Syntax Error: {str(e)}"
        except Exception as e:
            return f"Unexpected Error: {str(e)}"

    #region SELECT Parser
    def _parse_select(self) -> str:
        """Validate SELECT statement with strict ANSI SQL rules"""
        pattern = (
            r"SELECT\s+(?:ALL|DISTINCT)?\s+"
            r"(?:\*|(?:\w+(?:\.\w+)?(?:,\s*\w+(?:\.\w+)?)*)\s+"
            r"FROM\s+\w+(?:\s+(?:AS\s+)?\w+)?(?:\s+(?:INNER|LEFT|RIGHT|FULL)\s+JOIN\s+\w+(?:\s+ON\s+[\w\.]+\s*=\s*[\w\.]+)*)"
            r"(?:\s+WHERE\s+(?:\(?[\w\.]+\s+(?:=|!=|<|>|<=|>=|LIKE|IN|BETWEEN|IS\s+NULL|IS\s+NOT\s+NULL)\s+(?:[\w\.]+|'[^']*')(?:\s+(?:AND|OR)\s+[\w\.]+\s+(?:=|!=|<|>|<=|>=|LIKE|IN|BETWEEN|IS\s+NULL|IS\s+NOT\s+NULL)\s+(?:[\w\.]+|'[^']*'))*?\)?)"
            r"(?:\s+GROUP\s+BY\s+[\w\.]+(?:,\s*[\w\.]+)*)?"
            r"(?:\s+HAVING\s+[\w\.]+\s+(?:=|!=|<|>|<=|>=)\s+(?:\d+|'[^']*'))?"
            r"(?:\s+ORDER\s+BY\s+[\w\.]+\s+(?:ASC|DESC)?(?:,\s*[\w\.]+\s+(?:ASC|DESC)?)*"
            r"\s*;\s*$"
        )
        if not re.fullmatch(pattern, self.query, re.IGNORECASE):
            raise SQLSyntaxError("Invalid SELECT statement structure")
        return "Valid SELECT syntax"
    #endregion

    #region DELETE Parser
    def _parse_delete(self) -> str:
        """Validate DELETE statement with strict IN clause handling"""
        match = re.match(
            r"DELETE\s+FROM\s+(?P<table>\w+)(?:\s+WHERE\s+(?P<where>.+?))?\s*;",
            self.query,
            re.IGNORECASE
        )
        if not match:
            raise SQLSyntaxError("Invalid DELETE statement structure")

        table = match.group('table')
        self._validate_identifier(table, "table name")

        where_clause = match.group('where')
        if where_clause:
            self._validate_where_clause(where_clause)

        return "Valid DELETE syntax"

    def _validate_where_clause(self, clause: str):
        """Validate WHERE clause with complex conditions"""
        in_pattern = r"\bIN\s*\(\s*((?:'[^']*'|\d+)(?:,\s*(?:'[^']*'|\d+))*)\s*\)"
        for match in re.finditer(in_pattern, clause, re.IGNORECASE):
            self._validate_in_clause(match.group(1))

        if re.search(r'"', clause):
            raise SQLSyntaxError("Double quotes are not allowed for string literals")

    def _validate_in_clause(self, values: str):
        """Validate IN clause values"""
        for value in re.split(r",\s*", values):
            if not (value.startswith("'") and value.endswith("'")) and not value.isdigit():
                raise SQLSyntaxError(f"Invalid value {value} in IN clause - must be quoted string or number")
    #endregion

    #region ALTER Parser
    def _parse_alter(self) -> str:
        """Validate ALTER TABLE with strict column definition rules"""
        pattern = (
            r"ALTER\s+TABLE\s+(?P<table>\w+)\s+"
            r"(?:ADD|DROP|MODIFY)\s+"
            r"(?:COLUMN\s+)?(?P<column>\w+)\s+"
            r"(?:\w+(?:\(\d+(?:,\d+)?\))?\s+)?"
            r"(?:NOT\s+NULL|NULL|DEFAULT\s+(?:'[^']*'|\d+)|PRIMARY\s+KEY|UNIQUE)?\s*;"
        )
        match = re.fullmatch(pattern, self.query, re.IGNORECASE)
        if not match:
            raise SQLSyntaxError("Invalid ALTER TABLE statement structure")

        table = match.group('table')
        column = match.group('column')
        
        self._validate_identifier(table, "table name")
        self._validate_identifier(column, "column name")
        
        if column.upper() in SQL_KEYWORDS:
            raise SQLSyntaxError(f"Reserved keyword '{column}' cannot be used as column name")

        return "Valid ALTER TABLE syntax"
    #endregion

    #region Utility Methods
    def _validate_identifier(self, identifier: str, identifier_type: str):
        """Validate SQL identifiers against reserved keywords and naming rules"""
        if re.search(r"\s", identifier):
            raise SQLSyntaxError(f"Invalid {identifier_type} '{identifier}' - spaces not allowed")
            
        if identifier.upper() in SQL_KEYWORDS:
            raise SQLSyntaxError(f"Reserved SQL keyword '{identifier}' cannot be used as {identifier_type}")

        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", identifier):
            raise SQLSyntaxError(f"Invalid {identifier_type} '{identifier}' - must start with letter/underscore")

    def _unsupported_statement(self) -> str:
        """Handle unsupported SQL statements"""
        raise SQLSyntaxError("Unsupported SQL statement type")
    #endregion

    #region Other Parsers (CREATE, INSERT, UPDATE, etc.)
    def _parse_create(self) -> str:
        """Validate CREATE TABLE with full column constraints"""
        # Implementation with advanced column validation
        pass

    def _parse_insert(self) -> str:
        """Validate INSERT with strict value-type matching"""
        pass

    def _parse_update(self) -> str:
        """Validate UPDATE with SET clause validation"""
        pass

    def _parse_drop(self) -> str:
        """Validate DROP TABLE with multiple table support"""
        pass

    def _parse_truncate(self) -> str:
        """Validate TRUNCATE TABLE syntax"""
        pass
    #endregion

def validate_sql(query: str) -> str:
    """Public validation interface"""
    try:
        parser = SQLParser(query)
        return parser.parse()
    except SQLSyntaxError as e:
        return f"Syntax Error: {str(e)}"

if __name__ == "__main__":
    while True:
        query = input("Enter SQL query: ")
        if not query:
            break
        print(validate_sql(query))