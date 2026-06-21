import requests
from pymongo import MongoClient

print("Fetching OpenPhish Feed...")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["threat_intelligence"]
collection = db["threat_indicators"]

try:
    response = requests.get(
        "https://openphish.com/feed.txt",
        timeout=10
    )

    print("Status Code:", response.status_code)

    if response.status_code == 200:

        urls = response.text.splitlines()

        inserted = 0

        for url in urls:

            # Check duplicates
            existing = collection.find_one(
                {"indicator": url}
            )

            if not existing:

                collection.insert_one({
                    "indicator": url,
                    "type": "URL",
                    "source": "OpenPhish",
                    "risk_score": 90
                })

                inserted += 1

        print(f"Inserted {inserted} new records into MongoDB")

    else:
        print("Request Failed")

except Exception as e:
    print("Error:", e)