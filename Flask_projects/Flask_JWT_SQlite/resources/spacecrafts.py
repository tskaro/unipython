from flask_jwt import jwt_required
from models.spacecrafts import Space_craft

class SpaceCraftForAPI(Space_craft):
    def get(self, item_id):
        value = Space_craft.find_by_id(item_id)
        if value:
            return value
        else:
            return {"message": f"ხომალდი id-ით {item_id} არ მოიძებნა"}

    @jwt_required()
    def post(self, item_id):
        ship_input = Space_craft.ship_parser.parse_args()
        if Space_craft.find_by_ship(ship_input['name']) or Space_craft.find_by_id(item_id):
            return "ship already exist!"
        else:
            Space_craft.insert(item_id, ship_input)
            return "ship has been added successfully"

    @jwt_required()
    def put(self, item_id):
        ship_input = Space_craft.ship_parser.parse_args()
        value = Space_craft.find_by_id(item_id)
        name_value = Space_craft.find_by_ship(ship_input['name'])
        if value:
            Space_craft.update(item_id, ship_input)
            return "Ship info has been edited"
        elif name_value:
            return f"To edit {ship_input['name']} go to id_ {name_value['id']}"
        else:
            Space_craft.insert(item_id, ship_input)
            return "New ship has been added successfully"