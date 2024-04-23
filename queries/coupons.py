from models import db, Coupon


def get_coupons():
    return Coupon.query.all()


def create_coupon(data):
    new_coupon = Coupon(**data)
    db.session.add(new_coupon)
    db.session.commit()
    return new_coupon
