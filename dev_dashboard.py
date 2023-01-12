import streamlit as st
import psycopg2

# Initialize connection.


def create_connection():
    try:
        conn = psycopg2.connect(
            host="172.17.84.48",
            user="asliri",
            password="pentaho2022.",
            database="log_db"
        )
        return conn
    except Exception as e:
        print("Error creating connection:", e)
        return None


conn = create_connection()

if conn:
    print("Connection established successfully!")
    curr = conn.cursor()
else:
    print("Error establishing connection.")


def run_query():
    try:
        query = "SELECT * FROM report_table limit 100;"
        curr.execute(query)
        print("Query executed successfully.")
        results = curr.fetchall()
        curr.close()
        return results
    except Exception as e:
        print("Error running query:", e)


results = run_query()
st.table(results)
