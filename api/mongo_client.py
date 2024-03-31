import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

MONGO_HOST = os.environ.get("MONGO_HOST", "mongo")
MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "root")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "")
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)
MONGO_DATABASE = os.environ.get("MONGO_DATABASE")


uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(
    MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST, MONGO_PORT, MONGO_DATABASE
)

mongo_client = MongoClient(uri)

print(mongo_client.nodes)
