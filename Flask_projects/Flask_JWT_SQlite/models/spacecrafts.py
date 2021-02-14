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