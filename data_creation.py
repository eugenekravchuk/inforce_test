from faker import Faker
import csv

def create_fake_users(output_path="data/users.csv"):
    fake = Faker()
    with open(output_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "name", "email", "signup_date"])
        for user_id in range(1, 1001):
            writer.writerow([user_id, fake.name(), fake.email(), fake.date_time_this_decade().isoformat()])

create_fake_users()