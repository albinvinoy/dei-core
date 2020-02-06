import os
from pymongo import MongoClient
from .app import  *


class MongoRepository(object):
    def __init__(self):
        super().__init__()
        mongo_url = os.environ.get("mongodb://127.0.0.1:27017/deicore")
        self.db = MongoClient(mongo_url)

    def find_all(self, selector):
        return self.db.find(selector)