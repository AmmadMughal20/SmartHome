from pickle import FALSE
from app import db
from datetime import datetime
from flask import request

class DHTData(db.Model):
    humidity = db.Column(db.String(10), index=True)
    temperature = db.Column(db.String(10), index=True)
    heat_index = db.Column(db.String(10), index=True)
    date_time = db.Column(db.String(10), index=True, primary_key=True)

    def _repr__(self):
        return '<Data {}>'.format(self.humidity,self.temperature,self.heat_index,self.date_time)

    def get_DHTData():
        data = DHTData.query
        return data
        
class UltrasonicData(db.Model):
    distance = db.Column(db.String(10), index=True)
    date_time = db.Column(db.String(10), index=True, primary_key=True)

    def _repr__(self):
        return '<Data {}>'.format(self.distance,self.date_time)

    def get_UltrasonicData():
        data = UltrasonicData.query
        return data