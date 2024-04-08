import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define a SQL query to select all tables in the database
select_tables_sql = "SELECT name FROM sqlite_master WHERE type='table';"

# Execute the SQL query
cursor.execute(select_tables_sql)

# Fetch all rows (tables) from the result set
tables = cursor.fetchall()

# Print the names of all tables
for table in tables:
    print(table[0])

# Close the cursor and connection
cursor.close()
conn.close()