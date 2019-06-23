from flask import Blueprint, request, jsonify
from flask_login import login_required

from models.climate import Climate

from datetime import datetime

climate = Blueprint('climate', __name__, template_folder='templates', static_folder='static')


@login_required
@climate.route('/temperature', methods=['GET'])
def temperature():
    dt_start = request.form.get('dtStart') or request.args.get('dtStart')
    dt_end = request.form.get('dtEnd') or request.args.get('dtEnd')
    sensor = request.form.get('sensor') or request.args.get('sensor')

    dt_start = datetime.strptime(dt_start, '%Y-%m-%d')
    dt_end = datetime.strptime(dt_end, '%Y-%m-%d')

    climate_data = Climate.query\
        .filter_by(sensor_id=sensor)\
        .filter(Climate.date >= dt_start)\
        .filter(Climate.date <= dt_end)\
        .all()

    temp = []
    hum = []
    date = []

    for data in climate_data:
        temp.append(data.temperature)
        hum.append(data.humidity)
        date.append(data.date)

    return jsonify({'temperature': temp, 'humidity': hum, 'date': date}), 200
