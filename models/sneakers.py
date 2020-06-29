import sqlite3
from .orm import ORM

class Listings(ORM):
    tablename = "sneaker"
    dbpath = ""

    def __init__(self, inv_key=1,sneaker_name='', year_released=1, version_num=1,orig_price=2.00, curr_price=3.00, manufacturer="", phone='', email='', creator=''):
        self.inv_key = inv_key
        self.sneaker_name = sneaker_name
        self.year_released = year_released
        self.version_num = version_num
        self.creator = creator
        self.orig_price = orig_price
        self.curr_price = curr_price
        self.manufacturer = manufacturer
        self.phone = phone
        self.email = email

    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            c = conn.cursor()
            row = f"""INSERT INTO {self.tablename} (
                sneaker_name, year_released, version_num,
                orig_price, curr_price, manufacturer, phone,
                email,creator) VALUES (?,?,?,?,?,?,?,?,?);"""
            values = (self.sneaker_name, self.year_released, self.version_num,
                    self.orig_price, self.curr_price, self.manufacturer, self.phone,
                    self.email,self.creator)
            c.execute(row, values)
            return True
        return False
    

    def update(self):        
        with sqlite3.connect(self.dbpath) as conn:
            c = conn.cursor()
            row = f"""UPDATE {self.tablename} SET 
                sneaker_name=?,year_released=?,version_num=?,
                orig_price=?,curr_price=?,manufacturer=?,phone=?,
                email=?,creator=? WHERE inv_key=?;"""
            values = (self.sneaker_name, self.year_released, self.version_num,
                    self.orig_price, self.curr_price, self.manufacturer, self.phone,
                    self.email,self.creator, self.inv_key)
            c.execute(row, values)
            return True
        return False