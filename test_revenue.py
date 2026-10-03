from src.database import get_connection

query = """
SELECT SUM(oi.quantity * oi.unit_price)
FROM orders AS o
JOIN order_items AS oi
    ON o.order_id = oi.order_id
WHERE o.status = 'completed';
"""

with get_connection() as conn:
    result = conn.execute(query).fetchone()
    print("Total completed-order revenue:", result[0])