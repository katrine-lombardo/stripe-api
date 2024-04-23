from flask import Blueprint, jsonify
import stripe

coupons = Blueprint("coupons", __name__)


@coupons.route("/coupons", methods=["GET"])
def get_coupons():
    coupons = stripe.Coupon.list(limit=3)
    return jsonify(coupons)
