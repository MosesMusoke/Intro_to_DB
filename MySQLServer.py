import mysql.connector
from mysql.connector import errorcode

# Database configuration
DB_NAME = 'alx_book_store'
DB_CONFIG = {
    'user': 'your_username',       # replace with your MySQL username
    'password': 'your_password',   # replace with your MySQL password
    'host': 'localhost',           # replace with your MySQL host if different
}

def create_database(cursor, db_name):
    try:
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database '{db_name}' already exists.")
        else:
            print(f"Failed to create database '{db_name}': {err}")

def main():
    try:
        # Establish a connection to MySQL server
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Create the database
        create_database(cursor, DB_NAME)
        
        # Commit the transaction
        conn.commit()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
