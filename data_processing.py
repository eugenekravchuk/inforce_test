import pandas as pd

def process_user_data(input_path="data/users.csv", output_path="data/cleaned_users.csv"):
    df = pd.read_csv(input_path, index_col="user_id")
    df["signup_date"] = pd.to_datetime(df["signup_date"]).dt.strftime("%Y-%m-%d")
    df = df[df["email"].str.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", na=False)]
    df["domain"] = df["email"].apply(lambda x: x.split("@")[1])
    df.to_csv(output_path, index=True)

process_user_data()
