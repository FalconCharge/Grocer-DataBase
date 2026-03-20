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