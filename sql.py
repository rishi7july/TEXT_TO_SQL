import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a Cursor
cursor = connection.cursor()

# Create a Table
table_info = '''
CREATE TABLE IF NOT EXISTS STUDENT (
    Name TEXT,
    Class TEXT,
    Section TEXT,
    Marks INTEGER
);
'''

cursor.execute(table_info)

# Insert data into the table
cursor.execute("INSERT INTO STUDENT VALUES ('Rishi', '5', 'B', 98)")
cursor.execute("INSERT INTO STUDENT VALUES ('Vrishali', 'C', 'B', 92)")
cursor.execute("INSERT INTO STUDENT VALUES ('Ved', '7', 'B', 100)")
cursor.execute("INSERT INTO STUDENT VALUES ('Virat', '8', 'B', 100)")
cursor.execute("INSERT INTO STUDENT VALUES ('Jairam', '9', 'B', 80)")
cursor.execute("INSERT INTO STUDENT VALUES ('Vihaan', '10', 'A', 75)")
cursor.execute("INSERT INTO STUDENT VALUES ('Shiv', '11', 'A', 90)")

# Select data from the table
data = cursor.execute("SELECT * FROM STUDENT WHERE Marks > 40")

# Print the result
for row in data:
    print(row)

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
