from flask import Flask
from flask_restful import Api
from resources import item_list, Space_craft, User_registration
from flask_jwt import JWT
from security import authentication, identity
app = Flask(__name__)
app.secret_key = "my_secret_key"

api = Api(app)
jwt = JWT(app, authentication, identity)

api.add_resource(item_list, '/item_list/')
api.add_resource(Space_craft, '/item/<int:item_id>')
api.add_resource(User_registration, '/registration')

if __name__ == '__main__':
    app.run(debug=True, port=500)