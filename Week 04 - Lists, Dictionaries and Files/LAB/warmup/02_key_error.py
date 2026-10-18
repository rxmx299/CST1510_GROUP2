# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}

print(record["label"]) # used an existing key

record["status"] = "OVER LIMIT" if record["value"] >= record["limit"] else "OK" # if you actually want the status value
print(record["status"])