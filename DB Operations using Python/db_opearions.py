import psycopg2
import os
from psycopg2 import sql
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

def connect_to_db():
    """Connect to the PostgreSQL database."""
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )

def create_database(db_name):
    """Create a new database."""
    conn = connect_to_db()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier(db_name)))
    cur.close()
    conn.close()

def delete_database(db_name):
    """Delete an existing database."""
    conn = connect_to_db()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(sql.SQL("DROP DATABASE IF EXISTS {};").format(sql.Identifier(db_name)))
    cur.close()
    conn.close()

def create_table():
    """Create a table."""
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT
        );"""
    )
    conn.commit()
    cur.close()
    conn.close()

def insert_data(name, age):
    """Insert data into the table."""
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s);", (name, age))
    conn.commit()
    cur.close()
    conn.close()

def retrieve_data():
    """Retrieve data from the table."""
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def delete_table_contents():
    """Delete contents of the table."""
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users;")
    conn.commit()
    cur.close()
    conn.close()

def create_table_with_python():
    """Create a table using Python."""
    create_table()

def insert_data_with_python():
    """Insert data into the table using Python."""
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    insert_data(name, age)

def extract_data_with_python():
    """Extract data from the database."""
    data = retrieve_data()
    for row in data:
        print(row)

# create_database('test_db')
# delete_database('test_db')
# create_table()
# insert_data('John Doe', 30)
# print(retrieve_data())
# delete_table_contents()
# create_table_with_python()
# insert_data_with_python()
# extract_data_with_python()
