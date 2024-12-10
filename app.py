import json
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Home Page
@app.route("/")
def home():
    session.pop('username', None)

    if 'username' in session:
        return redirect(url_for('menu'))
    return render_template("home.html")

@app.route("/register")
def registerapp():
    session.pop('username', None)

    if 'username' in session:
        return redirect(url_for('menu'))
    return render_template("register.html")

# Login
@app.route("/register", methods=['POST'])
def register():

    username = request.form['username']
    password = request.form['password']

    with sqlite3.connect("restaurant1213.db") as con:
        cur = con.cursor()

        cur.execute("INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')")

        con.commit()

        session['username'] = username
        
        return redirect(url_for('menu'))

# Login
@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    with sqlite3.connect("restaurant1213.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()
        if user:
            session['username'] = username
            return redirect(url_for('menu'))
        else:
            error = "Invalid credentials. Please try again."
            return render_template("home.html", error=error)

# Logout
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# Menu Page
@app.route("/menu")
def menu():
    if 'username' not in session:
        return redirect(url_for('home'))
    return render_template("menu.html")

# Menu Page
@app.route("/Restaurant")
def Res():
    if 'username' not in session:
        return redirect(url_for('home'))
    return render_template("Restaurant.html")



# Place Order
@app.route("/place_order", methods=['POST'])
def place_order():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    order_details = request.form['order_details']
    total_price = request.form['total_price']
    #taxAmount=request.form['taxAmount']
    customer_name = session['username']
    
    with sqlite3.connect("restaurant1213.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO orders (customer_name, order_details, total_price) VALUES (?, ?, ?)", 
                    (customer_name, order_details, total_price))
        con.commit()
       

    # Input JSON string
    json_string = order_details

    # Parse the JSON string into a Python list of dictionaries
    items = json.loads(json_string)

    # Access the first item in the list
    item = items[0]  # {'name': 'Burger', 'price': 12}
    name = item['name']  # "Burger"
    price = item['price']  # 12

    # Output the variables
    print("Name:", name)
    print("Price:", price)

    
    return render_template("order_confirmation.html", name=name, price=price, total_price=total_price)

# View Orders
@app.route("/orders")
def orders():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    with sqlite3.connect("restaurant.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM orders WHERE customer_name=?", (session['username'],))
        orders = cur.fetchall()
    
    return render_template("orders.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True)
