import streamlit as st
import psycopg2

# Initialize connection.


def create_connection():
    try:
        connection = psycopg2.connect(
            host="172.17.84.48",
            user="asliri",
            password="pentaho2022.",
            database="log_db"
        )
        return connection
    except Exception as e:
        print("Error creating connection:", e)
        return None


conn = create_connection()

if conn:
    print("Connection established successfully!")
else:
    print("Error establishing connection.")


# # Execute a SQL query
# query = "SELECT * FROM report_table limit 100;"
# cursor = conn.cursor()
# cursor.execute(query)

# # Fetch the results
# results = cursor.fetchall()

# # Close the cursor and connection
# cursor.close()
# conn.close()

# # Display the results in a Streamlit table
# st.table(results)
