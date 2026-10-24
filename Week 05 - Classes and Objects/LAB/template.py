"""
RECORD CHECK  -  my version
===========================

Name  : Rama Ehab 
Lane  : AI 
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# THRESHOLD (separate):
class Record:
    def __init__(self, label, value, limit):
        """store the dataset name, rows loaded and rows expected."""
        self.label = label
        self.value = value
        self.limit = limit


# create two Record objects 
records = [
    Record("survey_1", 1187, 1200),
    Record("survey_2", 1050, 1000),
]

# print a bordered report for each record
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f"Dataset      : {record.label}")
    print(f"Rows loaded  : {record.value}")
    print(f"Rows expected: {record.limit}")
    print("=" * 34)

# EXCELLENT(that includes all levels):
class Record:
    # one shared count for all Record objects
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """store the dataset name, rows loaded and rows expected."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """return the record's status and count OVER LIMIT results."""
        percent = (self.value / self.limit) * 100

        # check the conditions and work out the status based on the percentage
        if percent >= 100:
            result = "OVER LIMIT"
        elif percent >= 90:
            result = "WARNING"
        else:
            result = "OK"

        # increase the shared count by 1 if the result is OVER LIMIT
        if result == "OVER LIMIT":
            Record.over_limit_count += 1

        return result


def load_records(path):
    """read a file and return a list of Record objects."""
    records = []

    # open the file and read each line
    with open(path) as f:
        for line in f:
            # remove the whitespace and separate the values at each comma
            label, value, limit = line.strip().split(",")

            # convert the numbers to floats and add the record to the list
            records.append(Record(label, float(value), float(limit)))

    return records


# create a file that includes the data with one record per line
with open("dataset_records.txt", "w") as f:
    f.write("survey_1,1187,1200\n")
    f.write("survey_2,1050,1000\n")
    f.write("survey_3,800,1000\n")

# load the Record objects from the file
records = load_records("dataset_records.txt")

# print a bordered report for each record
for record in records:
    # call the status once for each record and store the result
    result = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f"Dataset      : {record.label}")
    print(f"Rows loaded  : {record.value}")
    print(f"Rows expected: {record.limit}")
    print(f"Status: {result}")
    print("=" * 34)

# print the total once after the loop
print(f"\n{Record.over_limit_count} of {len(records)} records are OVER LIMIT")