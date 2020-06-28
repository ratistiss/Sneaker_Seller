import sqlite3
import os

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "sneakers.db")
print(DATAPATH)

def schema():
    with sqlite3.connect(DATAPATH) as conn:
        cursor = conn.cursor()

        sql = """CREATE TABLE IF NOT EXISTS sneaker (
                inv_key INTEGER PRIMARY KEY AUTOINCREMENT,
                sneaker_name VARCHAR,
                year_released INTEGER,
                version_num INTERGER,
                orig_price FLOAT,
                curr_price FLOAT,
                manufacturer VARCHAR,
                phone VARCHAR,
                email VARCHAR,
                creator VARCHAR)"""

        cursor.execute(sql)


if __name__ == "__main__":
    schema()
