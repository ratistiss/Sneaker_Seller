from routes.route import app
from models.list_sneakers import Listings

Listings.dbpath = ""

app.run(debug=True)