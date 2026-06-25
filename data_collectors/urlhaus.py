import requests
from pymongo import MongoClient

def collect_urlhaus():

    print("Fetching URLhaus Feed...")

    client = MongoClient("mongodb://localhost:27017/")
    db = client["threat_intelligence"]
    collection = db["threat_indicators"]

    response = requests.get(
        "https://urlhaus.abuse.ch/downloads/text/",
        timeout=20
    )

    if response.status_code == 200:

        urls = response.text.splitlines()

        inserted = 0

        for item in urls[:100]:

            if item.startswith("#") or item.strip() == "":
                continue

            existing = collection.find_one(
                {"indicator": item}
            )

            if not existing:

                collection.insert_one({
                    "indicator": item,
                    "type": "URL",
                    "source": "URLhaus",
                    "risk_score": 95
                })

                inserted += 1

        print(f"URLhaus: {inserted} records inserted")

        return inserted

    return 0