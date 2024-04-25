# Stripe Reporting

## Motivation
A friend of mine wanted a way to pull resports on specific fields related to her company's subscription types, so I'm using this as a learning opportunity for interacting with external APIs.

## How it works
I used python for the data processing and database insertion. The first file "subscription_schedules" uses the Stripe module to collect the subscription data, and iterates through the paginated results using the auto-paging method. Data elements are added to a Pandas Dataframe, and then specific data pieces are transformed into the desired output for my Postgres database table. The dataframe is loaded into my postgres database using SQLAlchemy to create a table in the database and append the results data as table rows. 

## Technologies Used

[![Stripe](https://img.shields.io/badge/Stripe-008C73?style=for-the-badge&logo=stripe&logoColor=white)](https://stripe.com/docs/api)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FCA121?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)


## Obstacles

- I wasn't sure of the best approach to solve the problem, and criminally over-engineered the solution.


## Learnings

- Though fruitless in the end, I learned how to build a Flask application from scratch and developed a backend that is able to communicate with an external API, as well as leaving space for custom API development.


## Future Development

- This project is still a work in progress, so I will update this section once I've been able to pull and query the reports I need.


## Getting the App Running

1. If you don't have one already, sign up for a Stripe account and activate it: 
  https://dashboard.stripe.com/register
2. Git clone into your local repository:
```sh
git clone (repo)
```
2. Change directory:
```sh
cd stripe-api
```
3. Replace required environment variables with your own:
```sh
STRIPE_USERNAME=
STRIPE_PASSWORD=
API_KEY=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_NAME=
```
   *Optional variables for use with Flask app:
```sh
ENDPOINT_SECRET=
CLI_ACCOUNT_ID
```
4. Start virtual environment:
```sh
python -m venv .venv
source .venv/bin/activate
```
5. Upgrade pip and install dependencies:
```sh
python -m pip install --upgrade
pip install -r requirements.txt
```
5. Start the data collection:
```sh
python subscription_schedules.py
```
