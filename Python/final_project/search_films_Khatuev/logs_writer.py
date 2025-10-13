import os
import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
mdb = client[os.getenv("MONGO_DB")]
collection = mdb[os.getenv("MONGO_COLLECTION")]

def log_search(search_type: str, params: dict, results_count: int):
    collection.insert_one({
        "timestap": datetime.datetime.utcnow().isoformat(),
        "search_type": search_type,
        "params": params,
        "results_count": results_count
    })

