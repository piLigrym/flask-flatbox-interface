from app import db


class Hub(db.Model):
    id = db.Column(db.String(512), primary_key=True)  # primary keys are required by SQLAlchemy
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
