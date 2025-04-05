import os
import pandas as pd
import time
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

def wait_for_postgres(engine, retries=10, delay=2):
    for i in range(retries):
        try:
            with engine.connect():
                print("Database is ready.")
                return
        except OperationalError:
            print(f"Waiting for DB... retry {i+1}/{retries}")
            time.sleep(delay)
    raise Exception("Could not connect to the database.")

def load_users_to_db(csv_path="data/cleaned_users.csv"):
    db_url = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine = create_engine(db_url)
    wait_for_postgres(engine)

    df = pd.read_csv(csv_path, index_col="user_id")
    create_table_query = """
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        signup_date DATE,
        domain TEXT
    );"""

    with engine.connect() as conn:
        conn.execute(text(create_table_query))
        conn.commit()

    df.reset_index(inplace=True)
    df.to_sql("users", engine, if_exists="append", index=False)

load_users_to_db()