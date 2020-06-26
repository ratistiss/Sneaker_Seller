import sqlite3
import os

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "sneakers.db")
print(DATAPATH)

def Schema():
    with sqlite3.connect(DATAPATH) as conn:
        c = conn.cursor()
        table = """CREATE TABLE IF NOT EXISTS sneaker (
                inv_key INTEGER PRIMARY KEY AUTOINCREMENT,
                sneaker_name VARCHAR(24),
                year_released INTEGER,
                version_num INTERGER,
                creator VARCHAR(24),
                orig_price FLOAT,
                curr_price FLOAT,
                manufacturer VARCHAR(16),
                phone VARCHAR(24),
                email VARCHAR
            )"""
        c.execute(table)


if __name__ == "__main__":
    Schema()
