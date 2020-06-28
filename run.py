from routes.route import app
from models.list_sneakers import Listings

Listings.dbpath = "/Users/manderson/Documents/Sneaker_Seller/Sneaker_Seller/database/sneakers.db"

app.run(debug=True)