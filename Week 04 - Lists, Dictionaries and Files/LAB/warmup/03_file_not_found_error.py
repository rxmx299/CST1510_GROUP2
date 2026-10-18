# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
# catch the missing file error, then print a message instead of crashing
try:
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("This file is not found.")