import mysql.connector
# Set up your SQL connection parameters
connection_config = {
    'user': 'SQL_user',
    'password': 'Password',
    'host': 'SQL_Host_IP',
    'database': 'SQL_Database_name'
}

# Connect to the Cloud SQL instance
connection = mysql.connector.connect(**connection_config)

# Execute a query to retrieve data from the table
query = 'SELECT * FROM demo_table'
cursor = connection.cursor()
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Process and print the retrieved data
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()