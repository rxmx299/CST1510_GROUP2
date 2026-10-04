"""
RECORD CHECK  -  my version
===========================

Name  : Rama Ehab
Lane  :  AI       
Date  : 3-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit_count = 0
while True:
    label = input("Enter label (or quit to stop): ")      # replace with an input() call
    if label.lower() == "quit":
        break
    value = float(input("Enter value: "))     # replace with an input() call, converted with float()
    limit = float(input("Enter limit:"))     # replace with an input() call, converted with float()

    # calculations:
    difference = limit - value   # replace with your calculation
    percent = (value / limit) * 100  # replace with your calculation


    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"

    else:
        status = "OK"


    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

# your report lines go here
    print(f"Value      : {value:>10.2f}")
    print(f"Limit      : {limit:>10.2f}")
    print(f"Difference : {difference:>10.2f}")
    print(f"Percent    : {percent:>10.2f}%")
    print(f"Status     : {status:>10}")
    print("=" * 34)

print(f"Number of records OVER LIMIT: {over_limit_count}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
