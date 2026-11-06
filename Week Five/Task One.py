"""
Task 01: Suspicious IP Address Manager using Lists
Course: COMP08101 Programming for Cyber Security - Lab Exercise 5
"""


def display_first_and_last(ip_list):
    """Display the first and last IP addresses in the list."""
    if ip_list:
        print(f"First IP address: {ip_list[0]}")
        print(f"Last IP address : {ip_list[-1]}")
    else:
        print("The list is empty.")


def add_ip(ip_list):
    """Ask the user for a new IP address and append it to the list."""
    new_ip = input("Enter an IP address to add: ").strip()
    ip_list.append(new_ip)
    print(f"{new_ip} has been added.")


def change_ip(ip_list):
    """Replace an existing IP address with a new one entered by the user."""
    old_ip = input("Enter the existing IP address you want to change: ").strip()
    if old_ip in ip_list:
        index = ip_list.index(old_ip)          # find the position of the old IP
        new_ip = input("Enter the replacement IP address: ").strip()
        ip_list[index] = new_ip                # lists are mutable, so we can overwrite
        print(f"{old_ip} has been changed to {new_ip}.")
    else:
        print(f"{old_ip} was not found, so nothing was changed.")


def remove_ip(ip_list):
    """Remove an IP address supplied by the user."""
    target = input("Enter the IP address to remove: ").strip()
    if target in ip_list:
        ip_list.remove(target)
        print(f"{target} has been removed.")
    else:
        print(f"{target} is not in the list.")


def search_ip(ip_list):
    """Report whether an IP address supplied by the user exists in the list."""
    target = input("Enter the IP address to search for: ").strip()
    if target in ip_list:                      # 'in' operator checks membership
        print(f"{target} IS in the suspicious list.")
    else:
        print(f"{target} is NOT in the suspicious list.")


def main():
    """Run each step of the task in order."""
    # 1. List of at least five suspicious IP addresses
    suspicious_ips = ["192.168.1.15", "10.0.0.23", "172.16.5.9",
                      "203.0.113.45", "198.51.100.77"]
    print("Initial list:", suspicious_ips)

    # 2. First and last addresses
    display_first_and_last(suspicious_ips)

    # 3. Add a new address
    add_ip(suspicious_ips)

    # 4. Change an existing address
    change_ip(suspicious_ips)

    # 5. Remove an address
    remove_ip(suspicious_ips)

    # 6. Total number of addresses
    print(f"Total number of IP addresses: {len(suspicious_ips)}")

    # 7. Search for an address
    search_ip(suspicious_ips)

    print("Final list:", suspicious_ips)


if __name__ == "__main__":
    main()
