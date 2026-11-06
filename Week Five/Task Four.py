"""
Task 04: Unique IP Address Analyser using Sets
Course: COMP08101 Programming for Cyber Security - Lab Exercise 5
"""


def add_ip(ip_set):
    """Add a user-supplied IP address (duplicates are ignored by sets)."""
    new_ip = input("Enter an IP address to add: ").strip()
    ip_set.add(new_ip)
    print(f"{new_ip} has been added.")


def remove_ip(ip_set):
    """Remove a user-supplied IP address if it exists."""
    target = input("Enter an IP address to remove: ").strip()
    if target in ip_set:
        ip_set.remove(target)   # remove() raises KeyError if missing, so check first
        print(f"{target} has been removed.")
    else:
        print(f"{target} is not in the set.")


def check_ip(ip_set):
    """Check whether a user-supplied IP address exists in the set."""
    target = input("Enter an IP address to check: ").strip()
    if target in ip_set:
        print(f"{target} exists in the set.")
    else:
        print(f"{target} does not exist in the set.")


def main():
    # 1. Collection (list) of IP addresses including duplicates
    log_entries = ["192.168.1.10", "10.0.0.5", "192.168.1.10",
                   "172.16.0.8", "10.0.0.5", "203.0.113.45", "172.16.0.8"]
    print(f"Log entries ({len(log_entries)}):", log_entries)

    # 2. Convert to a set - duplicates are removed automatically
    unique_ips = set(log_entries)

    # 3. Display unique addresses (order may vary as sets are unordered)
    print("Unique IP addresses:", unique_ips)

    # 4. Add a new address
    add_ip(unique_ips)

    # 5. Remove an address
    remove_ip(unique_ips)

    # 6. Check membership
    check_ip(unique_ips)

    # 7. Number of unique addresses
    print(f"Number of unique IP addresses: {len(unique_ips)}")
    print("Final set:", sorted(unique_ips))


if __name__ == "__main__":
    main()
