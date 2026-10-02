
import unittest

from src.database import get_connection


class TestAnalyticsDatabase(unittest.TestCase):

    def test_expected_record_counts(self):
        expected = {
            "customers": 5,
            "products": 5,
            "orders": 6,
            "order_items": 10,
        }

        with get_connection() as conn:
            for table, expected_count in expected.items():
                with self.subTest(table=table):
                    actual_count = conn.execute(
                        f"SELECT COUNT(*) FROM {table}"
                    ).fetchone()[0]

                    self.assertEqual(actual_count, expected_count)

    def test_foreign_key_integrity(self):
        with get_connection() as conn:
            violations = conn.execute(
                "PRAGMA foreign_key_check"
            ).fetchall()

        self.assertEqual(violations, [])

    def test_completed_order_revenue(self):
        query = """
        SELECT SUM(oi.quantity * oi.unit_price)
        FROM orders AS o
        JOIN order_items AS oi ON o.order_id = oi.order_id
        WHERE o.status = 'completed';
        """

        with get_connection() as conn:
            actual_revenue = conn.execute(query).fetchone()[0]

        self.assertAlmostEqual(actual_revenue, 128200.0)


if __name__ == "__main__":
    unittest.main()