from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module
import sqlite3
from models import init_db
from utils import query_products

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Initialize the database
init_db()

@app.route("/")
def home():
    return "Welcome to the E-commerce Sales Chatbot API! Use the '/chat' endpoint to interact."

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    response = "Sorry, I didn't understand. Please use 'search product_name'."

    if "search" in user_message:
        keyword = user_message.split("search")[-1].strip()
        products = query_products(keyword)
        if products:
            response = "\n".join([f"{p[0]} - ${p[1]}" for p in products])
        else:
            response = f"No products found for '{keyword}'."

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)

