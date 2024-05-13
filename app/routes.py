from app import app
import requests
from flask import render_template,request,redirect,url_for #sluzy do wywolania pliku html

#flask - serwer
#istnieje cos takiego jak jinja

@app.route('/')
#@app.route('/index')
def index():
    return render_template("index.html.jinja")

@app.route('/extract', methods=['POST','GET'])
def extract():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        url=f'https://www.ceneo.pl/{product_id}'
        response= requests.get(url)
        if response.status_code == requests.codes['ok']:
            #musza istniec opinie
            #proces ekstrakcji opinii
            return redirect(url_for('product', product_id=product_id))
    return render_template("extract.html.jinja")

@app.route('/products')
def products():
    return render_template("products.html.jinja")

@app.route('/author')
def author():
    return render_template("author.html.jinja")

@app.route('/product/<product_id>')
def product(product_id):
    return render_template("product.html.jinja", product_id=product_id)

#@app.route('/hello')
@app.route('/hello/<name>')
def hello(name="world"):
    return f"Hello, {name}!"
