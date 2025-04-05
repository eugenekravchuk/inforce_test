# INFORCE DATA ENGINEERING TASK

This project implements a simple ETL pipeline that extracts data from a CSV file, transforms it, and loads it into a PostgreSQL database using Docker.

---

## Prerequisites

- Docker
- Docker Compose

---

## Installation

```bash
git clone https://github.com/eugenekravchuk/inforce_test
cd inforce_test
```

---

## Assumptions

- All input data is synthetically generated and clean except for intentional invalid emails.
- Email validation uses a simple regex pattern and may not cover all edge cases.
- The domain field is extracted by splitting on "@" — assumes all valid emails contain one "@".
- The ETL pipeline is expected to run once per container session (not a long-running service).
- PostgreSQL is assumed to be available via Docker Compose at hostname `db`.

## Usage and Verifying assumptions

### 1. Run the ETL pipeline with Docker Compose

```bash
docker-compose up --build
```

This will:

- Start a PostgreSQL container (`postgres_etl`)
- Build and run the ETL app container (`etl_app`)
- Generate fake user data
- Clean and transform it
- Load it into the `users` table in `users_db`

---

### 2. Connect to PostgreSQL inside the container

```bash
docker exec -it postgres_etl psql -U myuser -d users_db
```

---

### 3. Run SQL Queries

You can manually execute any of the queries stored in the `sql_scripts/` folder.

Example:

```sql
SELECT * FROM users LIMIT 5;
```

Or use:

```bash
docker exec -it postgres_etl psql -U myuser -d users_db -f /sql_scripts/query1_signup_counts.sql
```

---

## SQL Queries Overview

All SQL files are located in the `sql_scripts/` folder.

| File                              | Description                                                                      |
| --------------------------------- | -------------------------------------------------------------------------------- |
| `query1_signup_counts.sql`        | Count of users who signed up on each date                                        |
| `query2_unique_domains.sql`       | List of unique email domains                                                     |
| `query3_recent_signups.sql`       | Users who signed up in the last 7 days                                           |
| `query4_most_common_domain.sql`   | Users with the most common domain                                                |
| `query5_filter_email_domains.sql` | Delete users not from specific domains (`gmail.com`, `yahoo.com`, `example.com`) |

---

## Database Schema

**Table: `users`**

| Column        | Type    | Description                  |
| ------------- | ------- | ---------------------------- |
| `user_id`     | INTEGER | Primary key                  |
| `name`        | TEXT    | Full name                    |
| `email`       | TEXT    | Email address                |
| `signup_date` | DATE    | Date when the user signed up |
| `domain`      | TEXT    | Extracted domain from email  |

---

## Project Structure

```
inforce_test/
├── data/                      # Stores raw and cleaned CSV files
├── python_scripts/            # ETL pipeline logic
│   ├── data_creation.py
│   ├── data_processing.py
│   └── database_creation.py
├── sql_scripts/               # SQL queries
│   ├── query1_signup_counts.sql
│   ├── query2_unique_domains.sql
│   ├── query3_recent_signups.sql
│   ├── query4_most_common_domain.sql
│   └── query5_filter_email_domains.sql
├── main.py                    # Pipeline entry point
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```
