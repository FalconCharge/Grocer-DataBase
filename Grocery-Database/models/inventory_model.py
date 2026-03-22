from db import get_db_connection
import random

def create_inventory_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id int auto_increment primary key,
            product_id int not null,
            location varchar(100) not null,
            stock_level int not null default 0,
            unique (product_id, location),
            foreign key (product_id) references products(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

def add_inventory(product_id, location, stock_level=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    if stock_level is None:
        stock_level = 0

    
    cursor.execute("""
        INSERT INTO inventory (product_id, location, stock_level)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE stock_level = %s
    """, (product_id, location, stock_level, stock_level))

    conn.commit()
    cursor.close()
    conn.close()

def remove_stock(product_id, stock_level=1):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Should have this fail is there is not enough stock (But someone else should also be checking that before removing it from the shelf)
    cursor.execute(
        """
        UPDATE inventory set stock_level = GREATEST(stock_level - %s)
        where product_id = %s
        """, (stock_level, product_id)
    )

    conn.commit()
    cursor.close()
    conn.close()

def get_all_inventory():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM inventory as i ORDER BY i.product_id")

    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result

def get_total_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT COUNT(*) as total_products FROM inventory")
    total_products = cursor.fetchone()['total_products']

    cursor.close()
    conn.close()

    return total_products

def get_product_ids():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("Select i.product_id from inventory as i")

    rows = cursor.fetchall()

    product_ids = []
    for row in rows:
        product_ids.append(row['product_id'])

    cursor.close()
    conn.close()
    return product_ids

def insert_random_stock_levels():

    product_ids = get_product_ids()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    for product_id in product_ids:
        stock_level = random.randint(0, 20)

        cursor.execute("UPDATE inventory set stock_level = %s where product_id = %s", (stock_level, product_id))

    conn.commit()
    cursor.close()
    conn.close()

def generate_inventory_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Grab all the products
    cursor.execute("SELECT id FROM products")
    product_ids = [row[0] for row in cursor.fetchall()]

    for product_id in product_ids:
        num_locations = random.randint(1, 3)

        for i in range(num_locations):

            if random.random() < 0.7:
                location = f"AISLE {random.randint(1, 10)}"
            else:
                location = "WAREHOUSE"

            stock_level = random.randint(0, 50)

            cursor.execute("""
                INSERT INTO inventory (product_id, location, stock_level)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE stock_level = VALUES(stock_level)
            """, (product_id, location, stock_level))

    conn.commit()
    cursor.close()
    conn.close()
    
    

