from flask import Flask
from middle_project.middle_project import craft_list

# შუალედურის სია გადმოვიტანე


app = Flask(__name__)

@app.route('/')
def hello():
    return 'გამარჯობა'

@app.route('/get')
def structure():
    return craft_list


app.run()
