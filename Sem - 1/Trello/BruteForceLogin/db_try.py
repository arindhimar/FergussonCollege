import pyodbc

# Replace with your actual connection details
server = 'sql.freeasphost.net'
database = 'fergusson_student_data'
username = 'fergusson_student_data'
password = 'Fergusson@99'

# Establish connection to SQL Server
try:
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    cursor = conn.cursor()

    # Example: Perform a SELECT query
    cursor.execute('SELECT TOP 10 * FROM your_table_name')  # Adjust query as per your database structure
    rows = cursor.fetchall()

    # Example: Print fetched data
    for row in rows:
        print(row)

except pyodbc.Error as e:
    print(f"Error connecting to database: {e}")

finally:
    # Close database connection
    if 'conn' in locals():
        conn.close()
        print("Database connection closed.")
