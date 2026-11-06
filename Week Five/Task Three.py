"""
Task 03: Security Incident Manager using Dictionaries
Course: COMP08101 Programming for Cyber Security - Lab Exercise 5
"""


def display_user_and_ip(incident):
    """Display the username and IP address using their keys."""
    print(f"Username  : {incident['username']}")
    print(f"IP address: {incident['ip_address']}")


def display_all(incident):
    """Display all remaining keys and values."""
    print("Keys  :", list(incident.keys()))
    print("Values:", list(incident.values()))
    for key, value in incident.items():         # items() gives key-value pairs
        print(f"  {key}: {value}")


def main():
    # 1. Create the dictionary
    incident = {
        "username": "jsmith",
        "ip_address": "203.0.113.45",
        "event_type": "Failed Login",
        "risk_level": "Medium",
    }

    # 2. Display username and IP address
    display_user_and_ip(incident)

    # 3. Add a new field called status
    incident["status"] = "Open"
    print("After adding status:", incident)

    # 4. Update the risk level
    incident["risk_level"] = "High"
    print("After updating risk level:", incident)

    # 5. Remove one field (event_type) using del
    del incident["event_type"]
    print("After removing event_type:", incident)

    # 6. Display all remaining keys and values
    display_all(incident)

    # 7. Total number of key-value pairs
    print(f"Total key-value pairs: {len(incident)}")


if __name__ == "__main__":
    main()
