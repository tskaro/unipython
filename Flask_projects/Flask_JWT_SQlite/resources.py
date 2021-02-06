from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

items = [
    {"id": 1, "name": "Jedi Starfighter", "speed": 1, "arm": 1, "capacity": 15, "quantity": 11},
    {"id": 2, "name": "Starship Enterprise", "speed": 15, "arm": 9, "capacity": 3000, "quantity": 6},
    {"id": 3, "name": "Millennium Falcon", "speed": 18, "arm": 10, "capacity": 10, "quantity": 8},
    {"id": 4, "name": "super galaxy gurren lagann", "speed": 30, "arm": 10, "capacity": 10000, "quantity": 1}
]


class item_list(Resource):
    def get(self):
        return jsonify(items)

    @jwt_required()
    def delete(self):
        items.clear()


class Space_craft(Resource):
    ship_parser = reqparse.RequestParser()
    ship_parser.add_argument("name", type=str, required=True, help="Ship needs a name")
    ship_parser.add_argument("quantity", type=int, required=True, help="You must enter quantity")
    ship_parser.add_argument("speed", type=int, required=False)
    ship_parser.add_argument("arm", type=int, required=False)
    ship_parser.add_argument("capacity", type=int, required=False)

    def get(self, item_id):
        for object in items:
            if item_id == object["id"]:
                return jsonify(object)
        return {"message": f"ხომალდი id-ით {item_id} არ მოიძებნა"}

    @jwt_required()
    def post(self, item_id):
        for item in items:
            if item_id == item["id"]:
                return {"message": f"ხომალდი id-ით {item_id} უკვე არსებობს"}

        object = Space_craft.ship_parser.parse_args()

        ship_name = object["name"]
        for item in items:
            if object["name"] == item["name"]:
                return {"message": f"ხომალდი სახელად {ship_name} უკვე არსებობს"}
        new_ship = {
            "id": item_id,
            "name": object["name"],
            "speed": object["speed"],
            "arm": object["arm"],
            "capacity": object["capacity"],
            "quantity": object["quantity"]
        }
        items.append(new_ship)
        return {"message": "Ship has been added successfully"}

    @jwt_required()
    def put(self, item_id):
        ship = Space_craft.ship_parser.parse_args()
        item_in_dict = next(filter(lambda item: item['id'] == item_id, items), None)
        print(item_in_dict)
        if item_in_dict:
            item_in_dict.update(ship)
            return "ship values had been updated"
        elif item_in_dict == None:
            new_ship = {
                "id": item_id,
                "name": ship["name"],
                "speed": ship["speed"],
                "arm": ship["arm"],
                "capacity": ship["capacity"],
                "quantity": ship["quantity"]
            }
            items.append(new_ship)
            return "Ship has been added successfully"


if __name__ == '__main__':
    print("resources!")
