import sqlite3
from pathlib import Path
DB_PATH=Path(__file__).resolve().parent.parent / "data" / "analytics.db"


def get_connection():
    """Create a connection to the analystics database."""

    DB_PATH.parent.mkdir(parents=True,exist_ok=True)

    conn=sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    """Create the e-commerce analytics schema."""

    schema = """
    CREATE TABLE IF NOT EXISTS customers(

       customer_id INTEGER PRIMARY KEY,
       customer_name TEXT NOT NULL ,
       email TEXT UNIQUE,
       region TEXT NOT NULL );


    CREATE TABLE IF NOT EXISTS products (

       product_id INTEGER PRIMARY KEY ,
       product_name TEXT NOT NULL,
       category TEXT NOT NULL,
       current_price REAL NOT NULL CHECK (current_price >= 0)
        );


    CREATE TABLE IF NOT EXISTS orders(
       order_id INTEGER PRIMARY KEY,
       customer_id INTEGER NOT NULL,
       order_date TEXT NOT NULL ,
       status TEXT NOT NULL 
       CHECK (status IN('completed','pending','cancelled')),
       FOREIGN KEY (customer_id)
       REFERENCES customers(customer_id)
        );


    CREATE TABLE IF NOT EXISTS order_items(
       order_item_id INTEGER PRIMARY KEY,
       order_id INTEGER NOT NULL ,
       product_id INTEGER NOT NULL,
       quantity INTEGER NOT NULL CHECK (quantity > 0),
       unit_price REAL NOT NULL CHECK (unit_price >= 0),
       FOREIGN KEY (order_id) REFERENCES orders(order_id),
       FOREIGN KEY (product_id) REFERENCES products(product_id)
       );
       """
   
    with get_connection() as conn:
       conn.executescript(schema)


if __name__ == "__main__":
    create_tables()
    print(f"Database created at : {DB_PATH}")
    print("TABLES CREATED SUCCESSFULLY")

