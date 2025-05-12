import boto3
import os

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")
FILE_PATH = "/opt/airflow/data/player_stats_2024-25.csv"
S3_KEY = "raw/player_stats.csv"

def upload_to_s3():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)
    print(f"Uploaded {FILE_PATH} to s3://{BUCKET_NAME}/{S3_KEY}")

if __name__ == "__main__":
    upload_to_s3()