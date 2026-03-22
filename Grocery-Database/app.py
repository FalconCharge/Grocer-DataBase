from flask import Flask, render_template, request, redirect, url_for

import time

from db import get_db_connection
from models.product_model import get_all_products, add_product, create_products_table, insert_product_syntheic_data
from models.order_model import get_all_orders, create_order_table, add_order, update_order_total, get_all_orders_with_customer_name, generate_syn_order_data, vertify_orders
from models.customer_model import create_customer_table, get_all_customers, add_customer, get_customer_id, insert_syn_customer_data
from models.inventory_model import create_inventory_table, get_all_inventory, add_inventory, generate_inventory_data
from models.order_items_model import create_table_order_items, get_all_order_items, add_order_item, generate_random_orders

from query.Orders import select_most_expensive_orders, customer_spending, get_low_stock, get_exp_products, get_most_popular_products

app = Flask(__name__)

@app.route("/")
def index():
    view = request.args.get("view", "orders")

    if view == 'orders':
        data = select_most_expensive_orders()
    elif view == "customer_spending":
        data = customer_spending()
    elif view == "low_stock":
        data = get_low_stock()
    elif view == "expensive_products":
        data = get_exp_products()
    elif view == "most_popular_product":
        data = get_most_popular_products()

        # Add stock


    # Get all the customers names | How many orders they have made | Total money spent | Account created at | AVG order price | Sort in Highest money spent


    # Overview of inventory
    # Total products in inventory | most popular product | avg price of all products

    # OVerview of stock
    # Display which stock is getting low (may just show this on the inventory page)


    return render_template("index.html", data=data, view=view)

@app.route("/customers", methods=["GET", "POST"])
def customers():
    error = None

    # If the form was submitted
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        email = request.form["email"]
        phone = request.form["phone"]

        # should work no matter what since they are all varchar()
        # But should check length (I don't wanna do that now)

        add_customer(name, address, email, phone)
        return redirect(url_for("customers"))

    customers = get_all_customers()
    return render_template("customers.html", customers=customers, error=error)

@app.route("/inventory", methods=["GET", "POST"])
def inventory():
    error = None

    # If the form was submitted
    if request.method == "POST":
        product_id = request.form["product_id"]
        location = request.form['location']
        stock_Level = request.form["stockLevel"]

        try:
            stock_Level = int(stock_Level)
            if stock_Level < 0:
                raise ValueError
        except ValueError:
            error = "Please enter a valid stock_level."

        if not error:
            add_inventory(product_id=product_id, location=location, stock_level=stock_Level)
            return redirect(url_for("inventory"))

    inventory = get_all_inventory()
    return render_template("inventory.html", inventory=inventory, error=error)

@app.route("/orders", methods=["GET", "POST"])
def orders():
    error = None

    # Will also need to add items that were on the order somehow
    if request.method == "POST":
        order_type = request.form["order_type"]
        customer_name = request.form["customer_name"]
        customer = get_customer_id(name=customer_name)

        if customer is None:
            error = "Invalid customer Name"
        else:
            customer_id = customer["id"]
            add_order(customer_id=customer_id, order_type=order_type)
            return redirect(url_for("orders"))

    orders = get_all_orders_with_customer_name()
    return render_template("orders.html", orders=orders, error=error)


@app.route("/products", methods=["GET", "POST"])
def products():
    error = None

    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        supplier = request.form["supplier"]

        try:
            price = float(price)
            if price < 0:
                raise ValueError
        except ValueError:
            error = "Please enter a valid positive price."

        if not error:
            product_id = add_product(name, price, supplier)
            add_inventory(product_id=product_id, location="NOT SET")       # Also add the product in the inventory 
            return redirect(url_for("products"))

    products = get_all_products()
    return render_template("products.html", products=products, error=error)

@app.route("/order_items", methods=["GET", "POST"])
def order_items():
    error = None

    # If adding an item to an order
    if request.method == "POST":
        order_id = request.form["order_id"]
        product_id = request.form["product_id"]
        quantity = request.form["quantity"]

        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            error = "Please enter a valid positive quantity."

        if not error:
            # Get product price at time of order
            products = get_all_products()
            product = next((p for p in products if str(p["id"]) == str(product_id)), None)
            if product:
                price = product["price"]
                add_order_item(order_id, product_id, quantity, price)
                update_order_total(order_id, price, quantity=quantity)
            else:
                error = "Product not found."

            if not error:
                return redirect(url_for("order_items"))

    orders = get_all_orders()
    products = get_all_products()
    order_items = get_all_order_items()

    return render_template(
        "order_items.html",
        orders=orders,
        products=products,
        order_items=order_items,
        error=error
    )

if __name__ == "__main__":

    # give the database a second to set up
    time.sleep(10)

    create_products_table()
    create_customer_table()
    create_order_table()
    create_inventory_table()
    create_table_order_items()

    # Insert product data
    if len(get_all_products()) < 5:
        insert_product_syntheic_data()

    # Insert inven data if not already there
    if len(get_all_inventory()) < 5: 
        generate_inventory_data()

    # Insert customer Data
    if len(get_all_customers()) < 5:    
        insert_syn_customer_data()

    # Insert Orders
    if len(get_all_orders()) < 5:
        generate_syn_order_data()

    # Inset order Items
    if len(get_all_order_items()) < 50:
        generate_random_orders()

    # Check order Items and sets the correct total on the order table
    vertify_orders()

    app.run(host="0.0.0.0", port=5000, debug=True)
