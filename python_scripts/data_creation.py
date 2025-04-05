import os
import csv
import random
from faker import Faker

def create_fake_users(output_path="data/users.csv"):
    fake = Faker()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    valid_domains = ["gmail.com", "yahoo.com", "example.com", "example.org", "company.com"]
    invalid_domains = ["invalid", "fake", "no-domain", ""]

    with open(output_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "name", "email", "signup_date"])

        for user_id in range(1, 1001):
            name = fake.name()
            date = fake.date_time_this_decade().isoformat()

            if random.random() < 0.9:
                domain = random.choice(valid_domains)
                email = f"{fake.user_name()}@{domain}"
            else:
                broken = random.choice([
                    fake.user_name(),
                    fake.user_name() + "@",
                    "@" + random.choice(invalid_domains),
                    fake.user_name() + "@." + random.choice(invalid_domains)
                ])
                email = broken

            writer.writerow([user_id, name, email, date])

create_fake_users()
