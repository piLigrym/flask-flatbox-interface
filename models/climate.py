from utils import Database

db = Database().get_instance()


class Climate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary keys are required by SQLAlchemy
    hub_id = db.Column(db.String(512), db.ForeignKey('hub.id'), nullable=False)
    sensor_id = db.Column(db.String(36), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)


