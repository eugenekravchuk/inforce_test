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

## Usage

### 1. Run the ETL pipeline with Docker Compose

```bash
docker-compose up --build
```

This will:

- Start a PostgreSQL container (`postgres_etl`)
- Build and run the ETL app container (`etl_app`)
- Create sample user data, process it, and insert it into the `users` table in `users_db`

---

### 2. Connect to PostgreSQL inside the container

```bash
docker exec -it postgres_etl psql -U myuser -d users_db
```

---

### 3. Run SQL queries

You can run any SQL query from the `sql_scripts/` folder.

Example:

```sql
SELECT * FROM users LIMIT 5;
```

---

## Project Structure

```
inforce_test/
├── data/                   # Stores raw and cleaned CSV files
├── python_scripts/         # ETL pipeline Python modules
├── sql_scripts/            # Optional SQL query examples
├── main.py                 # Pipeline entry point
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## ✅ Notes

- The `data/` folder is created at runtime if it doesn't exist.
- The PostgreSQL container persists data using Docker volumes (`postgres_data`).
