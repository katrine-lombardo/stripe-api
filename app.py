# Run the server on http://localhost:4242
# >>> flask run --port=4242


from dotenv import load_dotenv
import os
import json
import stripe
from flask import Flask
from models import db
from routes import subscription_schedules, coupons, webhooks


load_dotenv()


# Configure Stripe API Key
stripe.api_key = os.getenv("API_KEY")

# Get Stripe CLI Webhook Secret
endpoint_secret = os.getenv("ENDPOINT_SECRET")

# Initialise Flask App
app = Flask(__name__)

# Register the Flask blueprints
app.register_blueprint(subscription_schedules)
app.register_blueprint(coupons)
app.register_blueprint(webhooks)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
