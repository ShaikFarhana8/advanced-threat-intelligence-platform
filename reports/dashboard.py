from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["threat_intelligence"]
collection = db["threat_indicators"]

print("=" * 55)
print("     ADVANCED THREAT INTELLIGENCE DASHBOARD")
print("=" * 55)

# Total Threats
total = collection.count_documents({})

# Source-wise Count
openphish = collection.count_documents({"source": "OpenPhish"})
urlhaus = collection.count_documents({"source": "URLhaus"})
alienvault = collection.count_documents({"source": "AlienVault"})

# Risk-wise Count
high = collection.count_documents({"risk_score": {"$gte": 90}})
medium = collection.count_documents({"risk_score": {"$gte": 70, "$lt": 90}})
low = collection.count_documents({"risk_score": {"$lt": 70}})

print(f"Total Threat Indicators : {total}")
print(f"OpenPhish Threats       : {openphish}")
print(f"URLhaus Threats         : {urlhaus}")
print(f"AlienVault Threats      : {alienvault}")

print("\nRisk Summary")
print("-" * 25)
print(f"High Risk   : {high}")
print(f"Medium Risk : {medium}")
print(f"Low Risk    : {low}")

print("\nLatest 10 Threat Indicators")
print("-" * 55)

latest = collection.find().sort("_id", -1).limit(10)

for threat in latest:
    print(
        f"{threat['source']:12} | "
        f"{threat['risk_score']} | "
        f"{threat['indicator']}"
    )

print("\nDashboard Generated Successfully.")