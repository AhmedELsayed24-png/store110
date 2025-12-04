
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_products():
    with open("products.json", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/product/<int:id>")
def product_page(id):
    return render_template("product.html", product_id=id)

@app.route("/api/products")
def api_products():
    return jsonify(load_products())

@app.route("/api/product/<int:id>")
def api_product(id):
    for p in load_products():
        if p["id"] == id:
            return jsonify(p)
    return jsonify({})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
