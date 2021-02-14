from flask import Flask
from flask_restful import Api
from models.spacecrafts import item_list
from resources.users import User_registration
from resources.spacecrafts import SpaceCraftForAPI
from flask_jwt import JWT
from security import authentication, identity


app = Flask(__name__)
app.secret_key = "my_secret_key"

api = Api(app)
jwt = JWT(app, authentication, identity)

api.add_resource(item_list, '/item_list/')
api.add_resource(SpaceCraftForAPI, '/item/<int:item_id>')
api.add_resource(User_registration, '/registration')

if __name__ == '__main__':
    app.run(debug=True, port=500)