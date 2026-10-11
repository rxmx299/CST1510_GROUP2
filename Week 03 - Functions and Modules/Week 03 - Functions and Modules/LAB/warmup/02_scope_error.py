# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status
# the variable status is defined inside the function, so it cannot be accessed outside the function so i added return status inside the function and assigned the returned value to status outside the function
status = check(87, 100)
print(status)
