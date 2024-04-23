from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Coupon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
