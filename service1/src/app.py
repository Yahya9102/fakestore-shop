from flask import Flask, jsonify
from client import fetch_products
from db import init_db, save_products, get_all_products


app = Flask(__name__)

init_db()

@app.get("/sync")
def fetch_and_save_products():
    products = fetch_products()
    save_products(products)
    return jsonify({"message": "all products fetched", "count": len(products)})


@app.get("/products")
def get_products():
    data = get_all_products()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
