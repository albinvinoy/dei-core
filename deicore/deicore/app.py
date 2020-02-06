import os
from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
client = MongoClient('mongodb://localhost:27017/deicore')
db = client.deicore
