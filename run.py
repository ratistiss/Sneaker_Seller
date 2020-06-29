from routes.route import app
from models.sneakers import Listings

Listings.dbpath = "database/sneakers.db"

app.run(debug=True)