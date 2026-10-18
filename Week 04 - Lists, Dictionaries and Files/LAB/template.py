"""
RECORD CHECK  -  my version
===========================

Name  : Rama Ehab
Lane  :  AI 
Date  : 17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# functions:

def check_record(value, limit):
    """Return the difference, percentage, and status for one record."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 80:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status,
                 message=None):
    """Print a bordered record report or a report message."""
    # print summaries and error messages here too
    if message is not None:
        print(message)
        return

    print()
    print("=" * 34)
    print(f"  RECORD CHECK -  {label}")
    print("=" * 34)
    print(f"  Used          : {value:>10.2f}")
    print(f"  Total         : {limit:>10.2f}")
    print(f"  Difference    : {difference:>10.2f}")
    print(f"  Percent       : {percent:>10.2f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 34)


def load_records(path):
    """Read records from a file and return a list of dictionaries."""
    records = []

    with open(path) as f:
        for line in f:
            # remove the newline and separate the values at each comma
            label, value, limit = line.strip().split(",")

            # create a dictionary for this record and add it to the list
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

    return records


# store:

filename = "datasets.txt"
# tested with nope.txt: FileNotFoundError was caught and a message was printed. The program continued with an empty list.
try:
    records = load_records(filename)
except FileNotFoundError:
    print_report(
        None, None, None, None, None, None,
        message=f"File not found: {filename}. Using an empty list."
    )
    records = []


# process + ouput:

over_count = 0

with open("dataset_results.txt", "w") as f:
    for record in records:
        # calculate the results for this record
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )

        # print a report for this record
        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        # write the label and status to the results file
        f.write(f"{record['label']},{status}\n")

        # count each record classified as OVER LIMIT
        if status == "OVER LIMIT":
            over_count += 1

# print the summary once, after the loop ends
print_report(
    None, None, None, None, None, None,
    message=f"{over_count} of {len(records)} were over limit"
)