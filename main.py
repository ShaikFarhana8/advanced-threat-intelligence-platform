from data_collectors.openphish import collect_openphish
from data_collectors.urlhaus import collect_urlhaus

print("=" * 50)
print("ADVANCED THREAT INTELLIGENCE PLATFORM")
print("=" * 50)

openphish_count = collect_openphish()

urlhaus_count = collect_urlhaus()

print("\nSummary")
print("-" * 20)
print("OpenPhish :", openphish_count)
print("URLhaus   :", urlhaus_count)
print("Total     :", openphish_count + urlhaus_count)
print("\nCollection Completed Successfully")