from app import app
from flask import render_template #sluzy do wywolania pliku html

#flask - serwer
#istnieje cos takiego jak jinja

@app.route('/')
#@app.route('/index')
def index():
    return render_template("index.html.jinja")

@app.route('/extract')
def extract():
    return render_template("extract.html.jinja")

@app.route('/products')
def products():
    return render_template("products.html.jinja")

@app.route('/author')
def author():
    return render_template("author.html.jinja")

@app.route('/product/<product_id>')
def product_id(product_id):
    return render_template("product.html.jinja", product_id=product_id)

#@app.route('/hello')
@app.route('/hello/<name>')
def hello(name="world"):
    return f"Hello, {name}!"
