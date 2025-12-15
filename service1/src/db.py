import sqlite3
from pathlib import Path


def set_db_path():
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "fakestore.sqlite"


def get_connection():
    conn = sqlite3.connect(set_db_path())
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            image TEXT NOT NULL
        )
        """        
    )

    conn.commit()
    conn.close()


def save_products(products):
    conn = get_connection()
    cur = conn.cursor()

    for p in products:
        cur.execute(
            """
            INSERT OR REPLACE INTO products (id, title, price, description, category, image)
            VALUES (?,?,?,?,?,?)
            """,
            (
                int(p["id"]),
                str(p["title"]),
                float(p["price"]),
                str(p["description"]),
                str(p["category"]),
                str(p["image"]),
            ),
        )


    conn.commit()
    conn.close()



def get_all_products():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, title, price, description, category, image from products ORDER BY id;")
    rows = cur.fetchall()

    conn.close()

    return [dict(row) for row in rows]

