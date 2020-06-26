import sqlite3


class Customers(Listings):

    def __init__(self, full_name, phone, email):       
        Listings.__init__(self,inv_key,name, year_released,version_num,creator,orig_price,curr_price,manufacturer)
            self.name = name
            self.phone = phone
            self.email = email
