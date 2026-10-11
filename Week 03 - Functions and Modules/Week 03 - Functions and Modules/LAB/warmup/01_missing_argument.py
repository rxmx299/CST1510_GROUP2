# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def status_of(percent, warning_at):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"
# the function requires two arguments, but only one is provided so i added 80 as the second argument
print(status_of(95,80))
