from app import app
from flask import render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html") 

@app.route('/extract' , methods=['POST','GET'])
def extract():
    if request.method == "POST":
        product_id = request.form.get('product_id')
        url = f"https://www.ceneo.pl/{product_id}"
        response = requests.get(url)
        if response.status_code == requests.codes['ok']:
            page_dom = BeautifulSoup(response)
            opinions_count =  page_dom = BeautifulSoup(response.text,"html.parser")
            try:
                opinions = page_dom.select_one("a.product-review__link > span").get_text().strip()
            except AttributeError:
                #proces extrakcji
                
                return redirect(url_for('product',product_id=product_id))
            error = "Produkt istnieje ale nie ma opini"
            return render_template("extract.html", error = error)
        error = "Błędny kod lub kod nie istnieje"
        return render_template("extract.html", error = error)
    return render_template("extract.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/author')
def author():
    return render_template("author.html")

@app.route('/product/<product_id>')
def product(product_id=" "):
    return render_template("product.html",product_id = product_id)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=""):
    return F"Hello, {name}!"