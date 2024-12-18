import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../database/ecomm.db")

def query_products(keyword):
    """
    Query products from the database based on a keyword.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM products WHERE LOWER(name) LIKE ?", ('%' + keyword.lower() + '%',))
    products = cursor.fetchall()
    conn.close()
    return products

