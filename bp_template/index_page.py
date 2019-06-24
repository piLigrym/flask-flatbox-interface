from flask import Blueprint, render_template, abort
from flask_login import login_required

from jinja2 import TemplateNotFound

from utils import Database
from models import Climate

index = Blueprint('index', __name__, template_folder='templates', static_folder='static')


@index.route('/')
@login_required
def render_recommendation():
    try:
        sensors = [r.sensor_id for r in Database().get_instance().session.query(Climate.sensor_id).distinct()]
        last = Climate.query.order_by(Climate.date.desc()).first()
        return render_template('charts.html',
                               sensors=sensors,
                               measurement=last)
    except TemplateNotFound:
        abort(404)
