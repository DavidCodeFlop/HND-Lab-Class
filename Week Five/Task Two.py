"""
Task 02: Security Incident Record using Tuples
Course: COMP08101 Programming for Cyber Security - Lab Exercise 5
"""


def display_items(record):
    """Display each element of the incident record individually."""
    print(f"Username   : {record[0]}")
    print(f"IP address : {record[1]}")
    print(f"Event type : {record[2]}")
    print(f"Severity   : {record[3]}")


def check_event(record, event):
    """Report whether a particular event type appears in the tuple."""
    if event in record:
        print(f"'{event}' appears in the incident record.")
    else:
        print(f"'{event}' does not appear in the incident record.")


def attempt_change(record):
    """Try to modify a tuple element and show the resulting error."""
    try:
        record[3] = "Low"   # tuples are immutable, so this raises TypeError
    except TypeError as error:
        print(f"Cannot modify the tuple -> TypeError: {error}")


def main():
    # 1. Create the tuple: (username, IP address, event type, severity)
    incident = ("jsmith", "203.0.113.45", "Failed Login", "High")
    print("Incident record:", incident)

    # 2. Display each item individually
    display_items(incident)

    # 3. Number of elements
    print(f"Number of elements: {len(incident)}")

    # 4. Check for an event type
    check_event(incident, "Failed Login")
    check_event(incident, "Malware Detected")

    # 5. Attempt to change an element
    attempt_change(incident)

    # Why tuples suit this: the record is fixed, so evidence cannot be altered.
    # Cyber security uses: audit log entries, (IP, port) socket pairs, and
    # fixed lists of blocked ports or protocols that must not change at runtime.


if __name__ == "__main__":
    main()
