"""
DuckDB execution layer.
Loads certified semantic SQL definitions from semantic layer.
"""

from pathlib import Path
import duckdb


DATA_PATH = Path("03_data/sample_data")
SEMANTIC_SQL_PATH = Path("02_semantic_layer/view_definitions")


def _register_base_tables(conn):
    """
    Register CSV files as DuckDB views.
    """

    conn.execute(f"""
        CREATE VIEW customers AS
        SELECT * FROM read_csv_auto('{DATA_PATH}/customers.csv');
    """)

    conn.execute(f"""
        CREATE VIEW accounts AS
        SELECT * FROM read_csv_auto('{DATA_PATH}/accounts.csv');
    """)

    conn.execute(f"""
        CREATE VIEW transactions AS
        SELECT * FROM read_csv_auto('{DATA_PATH}/transactions.csv');
    """)

    conn.execute(f"""
        CREATE VIEW products AS
        SELECT * FROM read_csv_auto('{DATA_PATH}/products.csv');
    """)


def _load_semantic_views(conn):
    """
    Load all certified semantic view SQL files.
    """

    for sql_file in SEMANTIC_SQL_PATH.glob("vw_*.sql"):
        view_sql = sql_file.read_text()
        conn.execute(view_sql)


def execute_query(sql: str):
    """
    Execute deterministic SQL against certified semantic views.
    """

    conn = duckdb.connect(database=":memory:")

    try:
        # Step 1: Register base physical tables
        _register_base_tables(conn)

        # Step 2: Load certified semantic views
        _load_semantic_views(conn)

        # Step 3: Execute incoming deterministic SQL
        result = conn.execute(sql).fetchall()
        columns = [desc[0] for desc in conn.description]

        rows = [dict(zip(columns, row)) for row in result]

        return rows

    finally:
        conn.close()


