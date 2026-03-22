from db import get_db_connection

def create_tracking_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracking(
            id int auto_increment primary key,
            order_id int not null,
            status varchar(100) default 'Pending',
            last_updated timestamp default CURRENT_TIMESTAMP
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
    tracking = cursor.fetchone()

    cursor.close()
    conn.close()
    return tracking

def add_tracking(order_id, status="Pending"):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tracking (order_id, Status) VALUES (%s, %s)",
        (order_id, status)
    )

    conn.commit()
    cursor.close()
    conn.close()
    return tracking_id

def update_tracking_status(tracking_id, status):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tracking SET Status = %s WHERE id = %s",
        (status, tracking_id)
    )

    conn.commit()
    cursor.close()
    conn.close()

def insert_tracking_synthetic_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""INSERT IGNORE INTO tracking (order_id, status) VALUES
    (1, 'Delivered'),
    (2, 'Shipped'),
    (3, 'Processing'),
    (4, 'Pending'),
    (5, 'Delivered'),
    (6, 'Shipped'),
    (7, 'Processing'),
    (8, 'Cancelled'),
    (9, 'Delivered'),
    (10, 'Pending')""")

    conn.commit()
    cursor.close()
    conn.close()
