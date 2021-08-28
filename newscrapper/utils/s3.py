from newscrapper.settings import S3
from boto3 import client

class S3Base(S3):
    def __init__(self):
        self.connect()

    def connect(self):
        self.client = client(super.url,aws_access_key_id=super.access_key, aws_secret_access_key=super.secret_access_key)

    def close(self):
        self.client.close()