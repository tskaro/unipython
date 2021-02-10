from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class item_list(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM ships')
        ships = cursor.fetchall()
        connection.commit()
        connection.close()
        return jsonify(ships)

    @jwt_required()
    def delete(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute('DELETE FROM ships')
        ships = cursor.fetchall()
        connection.commit()
        connection.close()


class Space_craft(Resource):
    ship_parser = reqparse.RequestParser()
    ship_parser.add_argument("name", type=str, required=True, help="Ship needs a name")
    ship_parser.add_argument("quantity", type=int, required=True, help="You must enter quantity")
    ship_parser.add_argument("speed", type=int, required=False)
    ship_parser.add_argument("arm", type=int, required=False)
    ship_parser.add_argument("capacity", type=int, required=False)



    @classmethod
    def find_by_id(cls, item_id):
        connection = sqlite3.connect("data.db")
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM ships where  id = ?', (item_id,))
        ships = cursor.fetchone()
        connection.commit()
        connection.close()
        if ships:
            return ships

    @classmethod
    def find_by_ship(cls, ship_name):
        connection = sqlite3.connect("data.db")
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM ships where  name = ?', (ship_name,))
        ships = cursor.fetchone()
        connection.commit()
        connection.close()
        if ships:
            return ships

    @classmethod
    def insert(cls, item_id, ship_input):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute('INSERT INTO ships VALUES(?,?,?,?,?,?)', (
            item_id, ship_input["name"], ship_input["speed"], ship_input["arm"], ship_input["capacity"],
            ship_input["quantity"]))
        connection.commit()
        connection.close()



    @classmethod
    def update(cls, item_id, ship_input):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute('UPDATE ships SET name = ?, speed = ? , arm =? , capacity = ? , quantity = ? WHERE id = ?',
                       (ship_input["name"], ship_input["speed"], ship_input["arm"], ship_input["capacity"],
                ship_input["quantity"], item_id))
        connection.commit()
        connection.close()


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



class User_registration(Resource):
    create_user_parser = reqparse.RequestParser()
    create_user_parser.add_argument("user_id", required=True, help="Enter your ID")
    create_user_parser.add_argument("username", required=True, help="Enter your username")
    create_user_parser.add_argument("password", required=True, help="Enter your password")

    def post(self):
        new_user = User_registration.create_user_parser.parse_args()
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?', (new_user['username'],))
        user_indb = cursor.fetchone()
        cursor.execute('SELECT * FROM users WHERE user_id=?', (new_user['user_id'],))
        id_indb = cursor.fetchone()
        if user_indb or id_indb:
            return "Username or id already exists"
        else:
            cursor.execute('INSERT INTO users Values(?,?,?)',
                           (new_user["user_id"], new_user["username"], new_user["password"]))
        connection.commit()
        connection.close()
        return "New user has been added"


if __name__ == '__main__':
    print("resources!")
