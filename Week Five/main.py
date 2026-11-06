"""
main.py
Uses the security_tools module to check a password and an IP address (Task 05).
Course: COMP08101 Programming for Cyber Security - Lab Exercise 5
"""

import getpass
import security_tools   # our own module, kept in the same folder


def main():
    # Ask the user for input (getpass hides the password as it is typed;
    # fall back to input() if no real terminal is available)
    try:
        password = getpass.getpass("Enter a password: ")
    except (EOFError, getpass.GetPassWarning):
        password = input("Enter a password: ")
    ip_address = input("Enter an IP address: ").strip()

    # Check the password
    password_ok, password_message = security_tools.validate_password(password)
    print(f"\nPassword check: {'VALID' if password_ok else 'INVALID'} - {password_message}")

    # If it is weak, suggest a strong randomly generated one
    if not password_ok:
        suggestion = security_tools.generate_password()
        print(f"Suggested strong password: {suggestion}")

    # Check the IP address
    ip_ok, ip_message = security_tools.validate_ip(ip_address)
    print(f"IP address check: {'VALID' if ip_ok else 'INVALID'} - {ip_message}")


if __name__ == "__main__":
    main()
