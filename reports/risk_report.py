from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["threat_intelligence"]

collection = db["threat_indicators"]

print("=" * 45)
print("THREAT INTELLIGENCE REPORT")
print("=" * 45)

total = collection.count_documents({})

openphish = collection.count_documents({
    "source": "OpenPhish"
})

urlhaus = collection.count_documents({
    "source": "URLhaus"
})

high_risk = collection.count_documents({
    "risk_score": {
        "$gte": 90
    }
})

print(f"Total Threat Indicators : {total}")
print(f"OpenPhish Indicators    : {openphish}")
print(f"URLhaus Indicators      : {urlhaus}")
print(f"High Risk Threats       : {high_risk}")