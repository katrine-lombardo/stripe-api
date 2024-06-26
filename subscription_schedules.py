"""
Get Stripe Subscription details

>>> python subscription_schedules.py
"""

import os
import requests
import pandas as pd
import stripe
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


# CONFIGURE
load_dotenv()

stripe.api_key = os.getenv("API_KEY")

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")


# EXTRACT
def extract() -> list:
    extracted_data = []
    try:
        data = stripe.SubscriptionSchedule.list(limit=10)
        for subscription_schedule in data.auto_paging_iter():
            extracted_data.append(subscription_schedule)
        return extracted_data
    except requests.exceptions.RequestException as e:
        print(f"Error extracting data: {e}")


# TRANSFORM
def transform(data_list: list) -> pd.DataFrame:
    dfs = []
    for data in data_list:
        subscription_schedule_data = {
            "id": data.get("id"),
            "created": data.get("created"),
            "customer": data.get("customer"),
            "status": data.get("status"),
        }
        df = pd.DataFrame([subscription_schedule_data])
        dfs.append(df)
    if dfs:
        print(f"Total number of subscription schedules: {len(dfs)}")
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame


# LOAD
def load(df: pd.DataFrame, table_name: str) -> None:
    engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}")
    if not df.empty:
        try:
            df.to_sql("subscription_schedules", engine, if_exists="replace")
            print(f"Data loaded into {table_name} table successfully.")
        except SQLAlchemyError as e:
            print(f"Error loading data into {table_name} table: {e}")
    else:
        print("Error: DataFrame is empty. No data to load.")


# EXECUTE
def main():
    try:
        data = extract()
        df = transform(data)
        if not df.empty:
            load(df, "subscription_schedules")
        else:
            print("Error: No data to load.")
    except SQLAlchemyError as e:
        print(f"An error occurred with SQLAlchemy: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
