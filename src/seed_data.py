
from src.database import get_connection, create_tables


def seed_data():
    """Insert sample e-commerce data into the database."""

    create_tables()

    customers = [
        (1, "Aarav Sharma", "aarav@example.com", "North"),
        (2, "Diya Verma", "diya@example.com", "South"),
        (3, "Kabir Singh", "kabir@example.com", "West"),
        (4, "Meera Gupta", "meera@example.com", "East"),
        (5, "Rohan Patel", "rohan@example.com", "North"),
    ]

    products = [
        (1, "Laptop", "Electronics", 55000.00),
        (2, "Headphones", "Electronics", 2500.00),
        (3, "Office Chair", "Furniture", 7000.00),
        (4, "Notebook", "Stationery", 100.00),
        (5, "Desk Lamp", "Furniture", 1200.00),
    ]

    orders = [
        (1, 1, "2026-01-15", "completed"),
        (2, 2, "2026-01-20", "completed"),
        (3, 3, "2026-02-05", "pending"),
        (4, 4, "2026-02-12", "completed"),
        (5, 5, "2026-03-01", "cancelled"),
        (6, 1, "2026-03-10", "completed"),
    ]

    order_items = [
        (1, 1, 1, 1, 54000.00),
        (2, 1, 2, 2, 2200.00),
        (3, 2, 3, 1, 6500.00),
        (4, 2, 4, 5, 90.00),
        (5, 3, 2, 1, 2500.00),
        (6, 4, 5, 2, 1100.00),
        (7, 4, 4, 10, 85.00),
        (8, 5, 1, 1, 55000.00),
        (9, 6, 1, 1, 53000.00),
        (10, 6, 3, 1, 6800.00),
    ]

    with get_connection() as conn:
        conn.executemany(
            """
            INSERT OR IGNORE INTO customers
            (customer_id, customer_name, email, region)
            VALUES (?, ?, ?, ?)
            """,
            customers,
        )

        conn.executemany(
            """
            INSERT OR IGNORE INTO products
            (product_id, product_name, category, current_price)
            VALUES (?, ?, ?, ?)
            """,
            products,
        )

        conn.executemany(
            """
            INSERT OR IGNORE INTO orders
            (order_id, customer_id, order_date, status)
            VALUES (?, ?, ?, ?)
            """,
            orders,
        )

        conn.executemany(
            """
            INSERT OR IGNORE INTO order_items
            (order_item_id, order_id, product_id, quantity, unit_price)
            VALUES (?, ?, ?, ?, ?)
            """,
            order_items,
        )

    print("Sample data seeding completed.")


if __name__ == "__main__":
    seed_data()