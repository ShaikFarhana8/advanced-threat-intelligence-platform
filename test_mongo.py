from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["threat_intelligence"]

collection = db["threat_indicators"]

data = {
    "indicator": "8.8.8.8",
    "type": "IPv4",
    "source": "test"
}

collection.insert_one(data)

print("Inserted Successfully")