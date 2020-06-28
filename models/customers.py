import sqlite3
from .orm import ORM 

class Customers(ORM):

    def __init__(self,phone, email, full_name, address):       
        super().__init__(self, phone, email)
        self.full_name = full_name
        self.address = address