import boto3
import os

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = "tb-nba-players-average-stats-2025"
FILE_PATH = "./data/nba_stats.csv"
S3_KEY = "raw/nba_stats.csv"

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
