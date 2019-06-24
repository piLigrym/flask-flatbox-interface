from flask import Blueprint, request, redirect, url_for
from flask_login import login_user, login_required, logout_user

from models import User

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')


@auth.route('/auth')
def login():
    name = request.form.get('name') or request.args.get('name')
    password = request.form.get('password') or request.args.get('password')

    user = User.query.filter_by(name=name).first()
    # TODO CHECK BY HASH
    # TODO FLASK MESSAGES
    if not user or not user.password == password:
        return redirect(url_for('login.render_login'))
    login_user(user, remember=True)
    return redirect(url_for('chart.render_chart'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.render_login'))
