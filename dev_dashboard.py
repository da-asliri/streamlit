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
cursor = conn.cursor()

if conn:
    print("Connection established successfully!")
else:
    print("Error establishing connection.")


def run_query():
    try:
        query = "SELECT * FROM report_table limit 100;"
        cursor.execute(query)
        cursor.close()
        conn.close()
        print("Query executed successfully.")
    except Exception as e:
        print("Error running query:", e)


run_query()
results = cursor.fetchall()

# # Display the results in a Streamlit table
st.table(results)
