from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    
    client.admin.command("ping")

    db = client["threat_intelligence"]

    collection = db["threat_indicators"]

    print("MongoDB Connected Successfully")

except Exception as e:
    print("Connection Failed")
    print(e)