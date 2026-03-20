from db import get_db_connection
from models.product_model import get_all_products
from models.order_model import get_all_orders
import random

def create_table_order_items():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            CREATE TABLE if not exists order_items (
                id int auto_increment primary key,
                order_id int not null,
                product_id int not null,
                quantity int not null default 1,
                price Decimal(10, 2) not null,

                unique(order_id, product_id),

                foreign key (order_id) references orders(id) on delete cascade,
                foreign key (product_id) references products(id)
            )
    """
    )

    conn.commit()
    cursor.close()
    conn.close()



def add_order_item(order_id, product_id, quantity, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO order_items (order_id, product_id, quantity, price)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)
    """, (order_id, product_id, quantity, price))
    
    conn.commit()
    cursor.close()
    conn.close()

def get_all_order_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("select * from order_items ORDER BY order_id")

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def generate_random_orders():
    randomP = []
    randomO = []

    for product in get_all_products():
        count = random.randint(1, 5) # how many times the products will appear
        for i in range(count):
            randomP.append(product)

    for order in get_all_orders():
        randomO.append(order['id'])

    random.shuffle(randomP)
    random.shuffle(randomO)
    
    # Generate a bunch of random combination of order's with products
    for order in randomO:
        if len(randomP) > 0:
            amountOfItems = random.randint(1, 5)
            for i in range(amountOfItems):
                if len(randomP) == 0:
                    break
                product = randomP.pop()
                randomQ = random.randint(1, 3)
                add_order_item(order, product['id'], randomQ, product['price'])




        