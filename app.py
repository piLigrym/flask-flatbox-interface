from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from utils.config import ParserConfig

import os

path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(path, 'config', 'config.json')
config = ParserConfig(config_path)

app = Flask(__name__)
app.config['SECRET_KEY'] = config['secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{password}@{host}:{port}/{database}'.format(
    **config['database'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

from bp_template.chart_page import chart
from bp_template.login_page import login
from bp_template.recommendation_page import recommendation
from bp_template.index_page import index

app.register_blueprint(chart)
app.register_blueprint(login)
app.register_blueprint(recommendation)
app.register_blueprint(index)

from bp_rest.auth import auth
from bp_rest.climate import climate
app.register_blueprint(auth)
app.register_blueprint(climate, url_prefix='/climate')


login_manager = LoginManager()
login_manager.login_view = 'login.render_login'
login_manager.init_app(app)

from models.user import User
from models.hub import Hub
from models.climate import Climate


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run()
