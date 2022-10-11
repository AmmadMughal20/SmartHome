from app import app
from flask import render_template, flash, redirect, url_for, request
from app.model import DHTData,UltrasonicData

@app.route('/')
@app.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    dhtdata = DHTData.get_DHTData().paginate()
    datacount = DHTData.get_DHTData().count()
    next_url = url_for('index', page=dhtdata.next_num) \
       if dhtdata.has_next else None
    prev_url = url_for('index', page=dhtdata.prev_num) \
       if dhtdata.has_prev else None
    return render_template('dht_sensor.html', title='Welcome - Smart Home', dhtdata=dhtdata.items,next_url=next_url,prev_url=prev_url,datacount=datacount) 

@app.route('/ultrasonic')
def ultrasonic():
    page = request.args.get('page', 1, type=int)
    ultrasonicdata = UltrasonicData.get_UltrasonicData().paginate()
    datacount = UltrasonicData.get_UltrasonicData().count()
    next_url = url_for('ultrasonic', page=ultrasonicdata.next_num) \
       if ultrasonicdata.has_next else None
    prev_url = url_for('ultrasonic', page=ultrasonicdata.prev_num) \
       if ultrasonicdata.has_prev else None
    return render_template('ultrasonic_sensor.html', title='Welcome - Smart Home', ultrasonicdata=ultrasonicdata.items,next_url=next_url,prev_url=prev_url,datacount=datacount) 
