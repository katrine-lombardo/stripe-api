from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SubscriptionSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)


