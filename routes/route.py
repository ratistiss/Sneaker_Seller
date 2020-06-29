from flask import Flask, request, jsonify
from models.sneakers import Listings


app = Flask(__name__)

@app.route("/test", methods=["GET"])
def show_status():
    return jsonify({"status": "success"})

@app.route("/all_items", methods=["GET"])
def show_list():
    whole_list = Listings.select_all()
    # python to change data structure here
    return jsonify({"Shoes": whole_list})    


@app.route("/add", methods=["POST"])
def add_item():
    data = request.get_json()
    if data is None:
        return jsonify({"success": False})
    new_listing = Listings(**data)
    success = new_listing.insert()
    return jsonify({"success": success})

@app.route("/update", methods=["POST"])
def update_item():
    data = request.get_json()
    if data is None:
        return jsonify({"success": False})
    new_listing = Listings(**data)
    success = new_listing.update()
    return jsonify({"success": success})

@app.route("/delete", methods=["POST"])
def delete_item():
    key = request.get_json().get("inv_key")
    if key is None:
        return jsonify({"success": False})
    success = Listings.delete(key)
    return jsonify({"success": success})

@app.route("/sort/phone", methods=["POST"])
def sort_person():
    key = request.get_json().get("phone")
    if key is None:
        return jsonify({"success": False})
    success = Listings.search_lister(key)
    return jsonify({"success": success})

@app.route("/sort/company", methods=["POST"])
def sort_company():
    key = request.get_json().get("manufacturer")
    if key is None:
        return jsonify({"success": False})
    success = Listings.search_maker(key)
    return jsonify({"success": success})

@app.route("/sort/price", methods=["POST"])
def sort_price():
    key = request.get_json().get("curr_price")
    if key is None:
        return jsonify({"success": False})
    success = Listings.search_price(key)
    return jsonify({"success": success})

@app.route("/sort/sale", methods=["POST"])
def sort_sale():
    key = request.get_json().get("curr_price", "orig_price")
    if key is None:
        return jsonify({"success": False})
    success = Listings.search_sales(key)
    return jsonify({"success": success})


if __name__ == "__main__":
    app.run()
