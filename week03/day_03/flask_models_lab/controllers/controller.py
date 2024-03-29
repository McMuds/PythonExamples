from flask import render_template

from app import app
from models.orders import order_list

@app.route('/')
def home():
    return render_template("index.html", title="Mario's", order_list=order_list)

@app.route('/orders')
def index():
    return render_template("index.html", title="Mario's", order_list=order_list)

@app.route('/orders/<orderid>')
def order(orderid):
    order_number = int(orderid)
    return render_template("order.html", title="Mario's", order=order_list[order_number])