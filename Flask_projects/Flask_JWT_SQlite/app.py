from flask import Flask
from flask_restful import Api
from resources import item_list, Space_craft

app = Flask(__name__)

api = Api(app)

api.add_resource(item_list, '/item_list/')

api.add_resource(Space_craft, '/item/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True, port=500)