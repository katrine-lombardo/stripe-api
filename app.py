# Run the server on http://localhost:4242
# >>> flask run --port=4242


from dotenv import load_dotenv
import os
import json
import stripe
from flask import Flask, jsonify, request
from models import db
from routes import subscription_schedules


load_dotenv()


# Configure Stripe API Key
stripe.api_key = os.getenv("API_KEY")

# Get Stripe CLI Webhook Secret
endpoint_secret = os.getenv("ENDPOINT_SECRET")

# Initialise Flask App
app = Flask(__name__)


# Register the flask blueprints
app.register_blueprint(subscription_schedules)


# Routes
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/webhook", methods=["POST"])
def webhook():
    event = None
    payload = request.data
    sig_header = request.headers["STRIPE_SIGNATURE"]

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        # Invalid payload
        raise e
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise e

    # Handle the event
    ## PLANS
    if event["type"] == "plan.created":
        plan = event["data"]["object"]
    elif event["type"] == "plan.deleted":
        plan = event["data"]["object"]
    elif event["type"] == "plan.updated":
        plan = event["data"]["object"]

    ## COUPONS
    elif event["type"] == "coupon.created":
        coupon = event["data"]["object"]
    elif event["type"] == "coupon.deleted":
        coupon = event["data"]["object"]
    elif event["type"] == "coupon.updated":
        coupon = event["data"]["object"]

    ## CHARGES
    elif event["type"] == "charge.captured":
        charge = event["data"]["object"]
    elif event["type"] == "charge.expired":
        charge = event["data"]["object"]
    elif event["type"] == "charge.failed":
        charge = event["data"]["object"]
    elif event["type"] == "charge.pending":
        charge = event["data"]["object"]
    elif event["type"] == "charge.refunded":
        charge = event["data"]["object"]
    elif event["type"] == "charge.succeeded":
        charge = event["data"]["object"]
    elif event["type"] == "charge.updated":
        charge = event["data"]["object"]
    elif event["type"] == "charge.dispute.closed":
        dispute = event["data"]["object"]
    elif event["type"] == "charge.dispute.created":
        dispute = event["data"]["object"]
    elif event["type"] == "charge.dispute.funds_reinstated":
        dispute = event["data"]["object"]
    elif event["type"] == "charge.dispute.funds_withdrawn":
        dispute = event["data"]["object"]
    elif event["type"] == "charge.dispute.updated":
        dispute = event["data"]["object"]
    elif event["type"] == "charge.refund.updated":
        refund = event["data"]["object"]

    ## SUBSCRIPTIONS
    elif event["type"] == "subscription_schedule.aborted":
        subscription_schedule = event["data"]["object"]
    elif event["type"] == "subscription_schedule.canceled":
        subscription_schedule = event["data"]["object"]
    elif event["type"] == "subscription_schedule.completed":
        subscription_schedule = event["data"]["object"]
    elif event["type"] == "subscription_schedule.created":
        subscription_schedule = event["data"]["object"]
    elif event["type"] == "subscription_schedule.expiring":
        subscription_schedule = event["data"]["object"]
    elif event["type"] == "subscription_schedule.released":
        subscription_schedule = event["data"]["object"]
    elif event["type"] == "subscription_schedule.updated":
        subscription_schedule = event["data"]["object"]

    ## OTHER
    else:
        print("Unhandled event type {}".format(event["type"]))

    return jsonify(success=True)


if __name__ == "__main__":
    app.run()
