from db import get_db_connection
import random

from models.order_model import get_all_orders

def create_tracking_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracking(
            id int auto_increment primary key,
            order_id int not null,
            status varchar(100) default 'Pending',
            last_updated timestamp default CURRENT_TIMESTAMP,
            foreign key (order_id) references orders(id)
        )""")

    conn.commit()
    cursor.close()
    conn.close()

def get_all_tracking():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tracking ORDER BY last_updated DESC")
    tracking = cursor.fetchall()

    cursor.close()
    conn.close()
    return tracking

def get_tracking_by_order(order_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tracking WHERE order_id = %s", (order_id,))
    tracking = cursor.fetchall()

    cursor.close()
    conn.close()
    return tracking

def add_tracking(order_id, status="Pending"):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tracking (order_id, status, last_updated) VALUES (%s, %s, CURRENT_TIMESTAMP)",
        (order_id, status)
    )
    
    tracking_id = cursor.lastrowid

    # Also update the order to ref the latest change
    cursor.execute(
        "UPDATE orders SET status = %s WHERE id = %s",
        (status, order_id)
    )

    conn.commit()
    cursor.close()
    conn.close()
    return tracking_id

def insert_tracking_synthetic_data():

    orders = get_all_orders()

    statuses = ["Processing", "Pending", "Cancelled"]


    conn = get_db_connection()
    cursor = conn.cursor()

    for order in orders:
            order_id = order["id"]

            status = random.choice(statuses)

            cursor.execute(
                "INSERT INTO tracking (order_id, status) VALUES (%s, %s)",
                (order_id, status)
            )

            latest_status = status

            # Randomly progress the order (simulate history)
            if status != "Cancelled" and random.random() < 0.55:
                cursor.execute(
                    "INSERT INTO tracking (order_id, status) VALUES (%s, %s)",
                    (order_id, "Shipped")
                )
                latest_status = "Shipped"

                if random.random() < 0.4:
                    cursor.execute(
                        "INSERT INTO tracking (order_id, status) VALUES (%s, %s)",
                        (order_id, "Delivered")
                    )
                    latest_status = "Delivered"

            # Update the order to reference correct status        
            cursor.execute(
                "UPDATE orders SET status = %s WHERE id = %s",
                (latest_status, order_id)
            )

    conn.commit()
    cursor.close()
    conn.close()
