import sqlite3

# Connect to SQLite
connection = sqlite3.connect("gold_rate.db")

# Create a cursor object
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE GOLD_RATE(
    DATE TEXT,
    CITY TEXT,
    GOLD_TYPE TEXT,
    RATE_PER_GRAM REAL
);
"""
cursor.execute(table_info)

# Insert sample gold rate records
cursor.execute("INSERT INTO GOLD_RATE VALUES('2025-04-10', 'Mumbai', '24K', 6150.50)")
cursor.execute("INSERT INTO GOLD_RATE VALUES('2025-04-10', 'Delhi', '22K', 5650.00)")
cursor.execute("INSERT INTO GOLD_RATE VALUES('2025-04-10', 'Chennai', '24K', 6135.75)")
cursor.execute("INSERT INTO GOLD_RATE VALUES('2025-04-10', 'Kolkata', '22K', 5620.25)")
cursor.execute("INSERT INTO GOLD_RATE VALUES('2025-04-10', 'Bangalore', '24K', 6140.00)")

# Display all the records
print("The inserted gold rate records are:")
data = cursor.execute("SELECT * FROM GOLD_RATE")
for row in data:
    print(row)

# Commit your changes to the database
connection.commit()
connection.close()
