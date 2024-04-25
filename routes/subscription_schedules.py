from flask import Blueprint, jsonify
import stripe

subscription_schedules = Blueprint("subscription_schedules", __name__)


@subscription_schedules.route("/subscription_schedules", methods=["GET"])
def get_subscription_schedules():
    schedules = stripe.SubscriptionSchedule.list(limit=10)
    return jsonify(schedules)
