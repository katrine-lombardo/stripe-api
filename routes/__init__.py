from flask import Blueprint

subscription_schedules = Blueprint("subscription_schedules", __name__)

from . import subscription_schedules_routes