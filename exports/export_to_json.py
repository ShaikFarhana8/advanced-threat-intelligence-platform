from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")

db = client["threat_intelligence"]

collection = db["threat_indicators"]

data = []

for threat in collection.find({}, {"_id": 0}):
    data.append(threat)

with open("exports/threat_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("=" * 50)
print("Threat data exported successfully!")
print(f"Total records exported: {len(data)}")
print("File saved as: exports/threat_data.json")