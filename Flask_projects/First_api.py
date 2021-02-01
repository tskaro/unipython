from flask import Flask, jsonify, request
from resources import items

app = Flask(__name__)


@app.route('/items')
def get_all():
    return jsonify(items)


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item_id == item["id"]:
            return jsonify(item), 200
    return {"message": f"ხომალდი id-ით {item_id} არ მოიძებნა"}, 404


@app.route('/items/<int:item_id>', methods=['POST'])
def post_item(item_id):
    for item in items:
        if item_id == item["id"]:
            return {"message": f"ხომალდი id-ით {item_id} უკვე არსებობს"}, 400  # შეასწორე კოდი
    ship = request.get_json()
    ship_name = ship["name"]
    for item in items:
        if ship["name"] == item["name"]:
            return {"message": f"ხომალდი სახელად {ship_name} უკვე არსებობს"}, 400  # შეასწორე კოდი
    new_ship = {
        "id": item_id,
        "name": ship["name"],
        "speed": ship["speed"],
        "arm": ship["arm"],
        "capacity": ship["capacity"],
        "quantity": ship["quantity"]
    }

    items.append(new_ship)
    return "Ship has been added successfully", 200



@app.route('/items/<int:item_id>', methods=['PUT'])
def put_item(item_id):
    ship = request.get_json()
    for item in items:
        if item_id == item["id"] and ship["name"] == item["name"]:
            item["speed"] = ship["speed"]
            item["arm"] = ship["arm"]
            item["capacity"] = ship["capacity"]
            item["quantity"] = ship["quantity"]
            return "Ship data has changed", 200
    for item in items:
        if item_id == item["id"] and ship["name"] != item["name"]:
            return "This id is dedicated to other ship", 400
    for item in items:
        if item_id != item["id"]:
            new_ship = {
                "id": item_id,
                "name": ship["name"],
                "speed": ship["speed"],
                "arm": ship["arm"],
                "capacity": ship["capacity"],
                "quantity": ship["quantity"]
            }
            items.append(new_ship)
            return "Ship has been added successfully", 200


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in items:
        if item_id == item["id"]:
            del items[item_id - 1]
            return "ship is deleted from the list", 200
    for item in items:
        if item_id != item["id"]:
            return "this id is not in the list", 400


if __name__ == "__main__":
    app.run(port=5324, debug=True)
