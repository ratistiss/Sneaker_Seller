from routes.route import app
from models.sneakers import Listings

Listings.dbpath = "data/sneakers.db"

app.run(debug=True)