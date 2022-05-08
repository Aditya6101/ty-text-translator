import os
from dotenv import load_dotenv
from pymongo import MongoClient
import datetime

# load .env file
load_dotenv()

# MONGO URI
MONGO_URI = os.getenv("MONGO_URI")

# estlablishing connection to mongodb using connection string
client = MongoClient(MONGO_URI)

print(client.server_info())

# getting database
db = client.text_translator_db

# getting collection
collection = db.text_translations

# posting

