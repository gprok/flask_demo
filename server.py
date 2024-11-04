from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("data.db")
db.execute("""CREATE TABLE IF NOT EXISTS products 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 name TEXT)
           """)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    product_list = cursor.execute("SELECT * FROM products")
    return render_template('products.html', products=product_list)

@app.route('/add/product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        data = request.form 
        product_name = data['product']
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name) VALUES ('" + product_name + "')")
        conn.commit()
        return redirect('/products')
    else:
        return render_template('add_product.html')


if __name__ == '__main__':
   app.run()