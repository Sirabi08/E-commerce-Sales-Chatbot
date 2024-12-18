import sqlite3
import os

# Generate an absolute path to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directory where models.py is located
DB_PATH = os.path.join(BASE_DIR, "../database/ecomm.db")

def init_db():
    """
    Initialize the database with mock product data.
    """
    if not os.path.exists(DB_PATH):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)  # Create database folder if it doesn't exist
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create products table
        cursor.execute('''
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        # Insert mock product data
        products = [
            ("Laptop", 999.99),
            ("Phone", 499.99),
            ("Headphones", 79.99),
            ("Book: Python Programming", 29.99),
            ("Tablet", 199.99),
            ("Monitor", 150.00)
        ]

        cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
        conn.commit()
        conn.close()
        print("Database initialized with product data.")
    else:
        print("Database already exists.")

print(f"Database Path: {DB_PATH}")

