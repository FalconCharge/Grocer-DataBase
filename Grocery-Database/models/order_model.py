from db import get_db_connection

import random

from models.customer_model import get_all_customers

def create_order_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id int not null,
            order_type varchar(100) default 'online',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total Decimal(10, 2) default 0,
            status VARCHAR(50) DEFAULT 'Processing',
            foreign key (customer_id) references customers(id)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

def update_order(order_id, order_type=None, total=None, status=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Could do this in one query by adding to a list and calling a query with the proper string but I'm slightly confused 
    # on it so I ain't doing it

    if order_type is not None:
        cursor.execute("Update orders as o SET o.order_type as %s where o.id = %s", (order_type, order_id))

    
    if total is not None:
        cursor.execute("UPDATE orders as o SET o.total as %s where o.id = %s", (total, order_id))

    # Might be a good Idead to vertify status is a proper value here
    if status is not None:
        cursor.execute("UPDATE orders AS o SET o.status as %s where o.id = %s", (status, order_id))

    conn.commit()
    cursor.close()
    conn.close()


def add_order(customer_id, order_type=None):
    conn = get_db_connection()
    cursor =  conn.cursor()

    cursor.execute("Insert into orders (customer_id, order_type) values (%s, %s)", (customer_id, order_type))
    
    order_id = cursor.lastrowid

    # Give it a tracking
    cursor.execute("INSERT INTO tracking (order_id, Status, last_updated) VALUES (%s, %s, CURRENT_TIMESTAMP)",
        (order_id, 'Processing')
    )

    conn.commit()


    cursor.close()
    conn.close()
    return order_id

def update_order_total(order_id, total, quantity):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        UPDATE orders set 
        total = total + (%s * %s) WHERE id = %s
        """, (total, quantity, order_id)
    )

    conn.commit()
    cursor.close()
    conn.close()

def get_all_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("Select * from orders ORDER BY id")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def vertify_orders():
    conn  = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        update orders as o
        JOIN (
            SELECT order_id, SUM(quantity * price) as total
            from order_items
            GROUP BY order_id
        ) as t ON o.id = t.order_id 
        SET o.total = t.total
        """
    )

    conn.commit()
    cursor.close()
    conn.close()

def get_all_orders_with_customer_name():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT c.name as customer_name, o.total, o.created_at, o.id, o.customer_id, o.status as status
        from orders as o
        join customers as c 
        ON o.customer_id = c.id ORDER BY o.id
        """
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def generate_syn_order_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    customers = get_all_customers()

    customer_ids = []
    order_id = 1
    
    for customer in customers:
        amoutOfOrders = random.randint(0, 2)
        for i in range(amoutOfOrders):
            customer_ids.append(customer["id"])

    random.shuffle(customer_ids)

    while(len(customer_ids) > 0):
        id = customer_ids.pop()
        order_id += 1
        cursor.execute("INSERT IGNORE INTO orders (id, customer_id, order_type) VALUES (%s, %s, %s)",
                       (order_id, id, 'online'))
        
        order_id = cursor.lastrowid


    conn.commit()
    cursor.close()
    conn.close()

