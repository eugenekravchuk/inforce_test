import os
import csv
from faker import Faker

def create_fake_users(output_path="data/users.csv"):
    fake = Faker()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "name", "email", "signup_date"])
        for user_id in range(1, 1001):
            writer.writerow([user_id, fake.name(), fake.email(), fake.date_time_this_decade().isoformat()])

create_fake_users()