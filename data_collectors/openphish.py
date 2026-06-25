import requests
from pymongo import MongoClient

def collect_openphish():

    print("Fetching OpenPhish Feed...")

    client = MongoClient("mongodb://localhost:27017/")
    db = client["threat_intelligence"]
    collection = db["threat_indicators"]

    response = requests.get(
        "https://openphish.com/feed.txt",
        timeout=10
    )

    if response.status_code == 200:
        urls = response.text.splitlines()
        inserted = 0

        for url in urls[:100]:
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

        print(f"OpenPhish: {inserted} records inserted")
        return inserted

    return 0