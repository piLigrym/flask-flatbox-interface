from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from utils import ParserConfig
from utils import Database

import os

path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(path, 'config', 'config.json')
config = ParserConfig(config_path)

app = Flask(__name__)
app.config['SECRET_KEY'] = config['secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{password}@{host}:{port}/{database}'.format(
    **config['database'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# init database singleton
db = Database()
db.get_instance().init_app(app)
migrate = Migrate(app, db.get_instance())

from bp_template import chart
from bp_template import login
from bp_template import recommendation
from bp_template import index

app.register_blueprint(chart)
app.register_blueprint(login)
app.register_blueprint(recommendation)
app.register_blueprint(index)

from bp_rest import auth
from bp_rest import climate
app.register_blueprint(auth)
app.register_blueprint(climate, url_prefix='/climate')


login_manager = LoginManager()
login_manager.login_view = 'login.render_login'
login_manager.init_app(app)

from models import User
from models import Hub
from models import Climate


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run()
