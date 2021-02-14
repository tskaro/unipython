from flask import jsonify
from flask_restful import Resource, reqparse
from datetime import datetime
import sqlite3


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
    Hinfo = reqparse.RequestParser()
    Hinfo.add_argument("Patient_id", type=str, required=True, help="Enter patient ID")
    Hinfo.add_argument("Glucose", type=int, required=True, help="Enter your latest blood glucose reading")
    Hinfo.add_argument("SBP", type=int, required=False)
    Hinfo.add_argument("DBP", type=int, required=False)

    @classmethod
    def insert(cls, patient_id, Hinfo):
        connection = sqlite3.connect("Health_data.db")
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Health_info(patient_id, Glucose, SBP, DBP, time) VALUES(?,?,?,?,?)', (
            patient_id, Hinfo["Glucose"], Hinfo["SBP"], Hinfo["DBP"], datetime.now().time()))
        connection.commit()
        connection.close()

