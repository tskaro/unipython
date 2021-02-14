from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import time
import sqlite3

# TODO: Create db in the app.py file over here to be sure

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Full_data(Resource):
    def get(self):
        connection = sqlite3.connect("Health_data.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Health_info')
        patient_data = cursor.fetchall()
        connection.commit()
        connection.close()
        return jsonify(patient_data)


class Patient_info(Resource):
    health_info = reqparse.RequestParser()
    health_info.add_argument("Glucose", type=int, required=True, help="Enter your latest blood glucose reading")
    health_info.add_argument("SBP", type=int, required=False)
    health_info.add_argument("DBP", type=int, required=False)

    @classmethod
    def insert(cls, patient_id, Hinfo):
        connection = sqlite3.connect("Health_data.db")
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Health_info(patient_id, Glucose, SBP, DBP, time) VALUES(?,?,?,?,?)', (
            patient_id, Hinfo["Glucose"], Hinfo["SBP"], Hinfo["DBP"], time.strftime('%Y-%m-%d %H:%M:%S')))
        connection.commit()
        connection.close()

    @classmethod
    def find_by_id(cls, patient_id):
        connection = sqlite3.connect("Health_data.db")
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Health_info WHERE patient_id = ?', (patient_id,))
        vitals = cursor.fetchall()
        print(vitals)
        connection.commit()
        connection.close()
        if vitals:
            return vitals
        
    def get(self, patient_id):
        vitals = Patient_info.find_by_id(patient_id)
        if vitals:
            return vitals
        else:
            return "Patient that you are searching does not exist"

    def post(self, patient_id):
        patient_vitals = Patient_info.health_info.parse_args()
        Patient_info.insert(patient_id, patient_vitals)
        return "Information has been added successfully"

# delete function deletes last entry of vital signs to undo invalid data entry
    def delete(self,patient_id):
        connection = sqlite3.connect("Health_data.db")
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Health_info WHERE row_id = (SELECT MAX(row_id) From Health_info WHERE patient_id =?)', (patient_id,))
        connection.commit()
        connection.close()
        return "Last entry has been deleted"

# TODO: I must add put method
    def put(self,patient_id):
        pass
        

app = Flask(__name__)
api = Api(app)

api.add_resource(Patient_info, '/vitals/<int:patient_id>')


if __name__ == '__main__':
    app.run(debug=True, port=500)