from newscrapper.settings import Database
from pymongo import MongoClient

class Base(Database):
    def __init__(self):
        self.connect()

    def connect(self):
        self.client = MongoClient(super().url)
    
    def close(self):
        self.client.close()