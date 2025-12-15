from flask import Flask, render_template
import requests

app = Flask(__name__)


SERVER1_BASE_URL = "http://service1:5001/products"





@app.get("/products")
def show_products():

    resp = requests.get(SERVER1_BASE_URL, timeout=10)
    resp.raise_for_status()

    products = resp.json()
    return render_template("products.html", products=products) 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
