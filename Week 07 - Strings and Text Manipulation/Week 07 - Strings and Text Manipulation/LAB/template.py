"""
RECORD CHECK  -  my version
===========================

Name  : Rama Ehab
Lane  :  AI 
Date  : 12/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Turn a messy survey line into a clean dictionary."""
    line = raw_line.strip().lower() # removes surrounding whitespace and converts to lowercase
    hostname_part, rest = line.split(",", 1) # separates the hostname from the fields
    hostname = hostname_part.strip() # removes remaining whitespace around the hostname

    # stores each cleaned key with its integer value
    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = int(value.strip())

    # returns one dictionary containing the hostname, rating, and age
    return {"hostname": hostname, "rating": fields["rating"], "age": fields["age"]}

def status_of(rating, age, warning_at=4):
    """Check the rating and age and return a status."""
    if age > 80 or rating > 5: # checks whether either value exceeds its limit
        return "OVER LIMIT"
    elif rating >= warning_at: # checks whether the rating reaches the warning value
        return "WARNING"
    else: # runs this if both the previous conditions are False
        return "OK"

# ====================================================================== INPUT
# reads the file and stores each raw line in a list
raw_records = []
with open("raw_records.txt") as f:
    for line in f:
        raw_records.append(line)
# =============================================================== PROCESS + OUTPUT
# starts both counters at zero
record_count = 0
flagged_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record) # converts the raw line into a clean dictionary
    status = status_of(record["rating"], record["age"]) # determines its status

    print(record, status) # prints the cleaned dictionary alongside its status

    record_count += 1 # counts each processed record

    if status != "OK": # counts both WARNING and OVER LIMIT records as flagged
        flagged_count += 1

# prints the total number of records and how many were flagged
print(f"Records: {record_count}, flagged: {flagged_count}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring 

# Invalid number test:
# print(parse_line("Survey_2031,rating=4,age=hello"))
# Error: invalid literal for int() with base 10: 'hello'
# explanataion: "hello" cannot be converted into an integer 