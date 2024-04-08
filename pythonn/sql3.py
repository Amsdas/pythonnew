import sqlite3

#Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')



#Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define the SQL command to create a table
create_table_sql = '''
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    department TEXT,
    salary REAL,
    hire_date DATE
);
'''

# Execute the SQL command to create the table
cursor.execute(create_table_sql)
# Commit the transaction
conn.commit()

# Close the connection
conn.close()



