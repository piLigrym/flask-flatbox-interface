from flask import Blueprint, render_template, abort
from flask_login import login_required

from jinja2 import TemplateNotFound


recommendation = Blueprint('recommendation', __name__, template_folder='templates', static_folder='static')


@recommendation.route('/recommendation')
@login_required
def render_recommendation():
    try:
        return render_template('recommendation.html')
    except TemplateNotFound:
        abort(404)
