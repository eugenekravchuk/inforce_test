from data_creation import create_fake_users
from data_processing import process_user_data
from database_creation import load_users_to_db

def run_pipeline():
    print("1. Creating fake users...")
    create_fake_users()

    print("2. Processing users...")
    process_user_data()

    print("3. Loading users to database...")
    load_users_to_db()

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
