import sqlite3


class ORM:

    @classmethod
    def delete(cls, pk):
        with sqlite3.connect(cls.dbpath) as conn:
            c = conn.cursor()
            row = f"""DELETE FROM {cls.tablename} WHERE inv_key=?;"""
            c.execute(row, (pk,))
            return True
        return False

    @classmethod
    def select_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            c = conn.cursor()
            row = f"""SELECT * FROM {cls.tablename}"""
            c.execute(row)
            results = c.fetchall()
            return results
        return []

    @classmethod
    def search_lister(cls, phone):
        with sqlite3.connect(cls.dbpath) as conn:
            c = conn.cursor()
            row = f"""SELECT * FROM {cls.tablename}
                    WHERE phone=?;"""
            c.execute(row,(phone,))
            results = c.fetchall()
            return results

    @classmethod
    def search_maker(cls, manufacturer):
        with sqlite3.connect(cls.dbpath) as conn:
            c = conn.cursor()
            row = f"""SELECT * FROM {cls.tablename}
                    WHERE manufacturer=?;"""
            c.execute(row,(manufacturer,))
            results = c.fetchall()
            return results

    @classmethod
    def search_price(cls, price):
        with sqlite3.connect(cls.dbpath) as conn:
            c = conn.cursor()
            row = f"""SELECT * FROM {cls.tablename}
                    WHERE curr_price<?;"""
            c.execute(row,(price,))
            results = c.fetchall()
            return results

    @classmethod
    def search_sales(cls, curr_price):
        with sqlite3.connect(cls.dbpath) as conn:
            c = conn.cursor()
            row = f"""SELECT curr_price, orig_price
                     FROM {cls.tablename}
                    WHERE curr_price <= .5 * orig_price;"""
            c.execute(row)
            results = c.fetchall()
            return results
            
            
        