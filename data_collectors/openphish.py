import requests
from pymongo import MongoClient
from utils.normalizer import normalize_indicator


def collect_openphish():

    print("Fetching OpenPhish Feed...")

    client = MongoClient("mongodb://localhost:27017/")
    db = client["threat_intelligence"]
    collection = db["threat_indicators"]

    try:
        response = requests.get(
            "https://openphish.com/feed.txt",
            timeout=10
        )

        if response.status_code == 200:

            urls = response.text.splitlines()

            inserted = 0

            for url in urls[:100]:

                if not url.strip():
                    continue

                existing = collection.find_one(
                    {"indicator": url}
                )

                if not existing:

                    threat = normalize_indicator(
                        indicator=url,
                        source="OpenPhish"
                    )

                    collection.insert_one(threat)

                    inserted += 1

            print(f"OpenPhish: {inserted} records inserted")

            return inserted

        else:
            print("Failed to fetch OpenPhish feed")
            return 0

    except Exception as e:
        print("Error:", e)
        return 0


if __name__ == "__main__":
    collect_openphish()