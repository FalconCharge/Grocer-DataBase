from db import get_db_connection

def select_most_expensive_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
            Select o.id, o.total, c.name as customer_name, o.created_at
            from orders as o 
            join customers as c ON c.id = o.customer_id
            ORDER BY o.total DESC
            LIMIT 10
        """
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def customer_spending():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT c.id, c.name, SUM(o.total) as total_spending, COUNT(o.id) as total_orders, c.created_at
        from customers as c
        join orders as o 
        ON o.customer_id = c.id 
        GROUP BY c.id
        ORDER BY total_spending DESC
        LIMIT 10    
        """
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return result

def get_low_stock():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT p.id AS product_id, p.name as product_name, i.stock_level as stock_level, i.location as location 
        from products as p
        join inventory as i ON p.id = i.product_id
        ORDER BY stock_level ASC
        LIMIT 15
"""
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def get_exp_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT p.id, p.name, p.price
        from products as p
        ORDER BY p.price DESC
        LIMIT 15
        """
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def get_most_popular_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT p.id as product_id, p.name as product_name, SUM(oi.quantity) as amount_in_carts, COUNT(DISTINCT oi.order_id) AS orders_contained
        from products as p
        join order_items as oi
        ON oi.product_id = p.id
        GROUP BY p.id, p.name
        ORDER BY amount_in_carts DESC
        LIMIT 20
        """
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result