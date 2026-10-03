from src.database import get_connection

with get_connection() as conn:
    query = """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
      AND name NOT LIKE 'sqlite_%'
    ORDER BY name;
    """

    tables = conn.execute(query).fetchall()

    print("Tables found:")
    for table in tables:
        print("-", table[0])