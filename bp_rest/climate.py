from flask import Blueprint, request, jsonify

from models import Climate

from utils import Database

from datetime import datetime

climate = Blueprint('climate', __name__, template_folder='templates', static_folder='static')


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


@climate.route('/add', methods=['POST'])
def climate_add():
    temp = request.form.get('tmp') or request.args.get('tmp') or request.json.get('tmp')
    humidity = request.form.get('hmd') or request.args.get('hmd') or request.json.get('hmd')
    sensor_id = request.form.get('sensor') or request.args.get('sensor') or request.json.get('sensor')
    date = datetime.now()

    try:
        climate_record = Climate()
        climate_record.temperature = float(temp)
        climate_record.humidity = float(humidity)
        # TODO: remove hardcoded id
        climate_record.hub_id = 1
        climate_record.sensor_id = int(sensor_id)
        climate_record.date = date

        Database().get_instance().session.add(climate_record)
        Database().get_instance().session.commit()

        return '', 200
    except Exception as e:
        return jsonify({'error': str(e)}), 501
