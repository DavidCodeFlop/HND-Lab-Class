"""
security_tools.py
Reusable cyber security utility functions (Task 05).
Course: COMP08101 Programming for Cyber Security - Lab Exercise 5
"""

import secrets
import string

MIN_PASSWORD_LENGTH = 10   # minimum length accepted by the validator


def validate_password(password):
    """
    Check a password for minimum length and variety.
    Returns (True/False, message explaining the result).
    """
    if len(password) < MIN_PASSWORD_LENGTH:
        return False, f"Too short - must be at least {MIN_PASSWORD_LENGTH} characters."

    # any() returns True if at least one character meets the condition
    has_letter = any(ch.isalpha() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_symbol = any(ch in string.punctuation for ch in password)

    if not has_letter:
        return False, "Must contain at least one letter."
    if not has_digit:
        return False, "Must contain at least one digit."
    if not has_symbol:
        return False, "Must contain at least one symbol."
    return True, "Password meets the requirements."


def validate_ip(ip_address):
    """
    Basic IPv4 format check: four numeric octets separated by three dots,
    each between 0 and 255. Returns (True/False, message).
    """
    octets = ip_address.split(".")
    if len(octets) != 4:                      # three dots means four parts
        return False, "Must contain exactly three dots (four octets)."

    for octet in octets:
        # isascii() stops non-standard Unicode digits being accepted
        if not (octet.isdigit() and octet.isascii()):
            return False, f"Octet '{octet}' is not a valid number."
        if not 0 <= int(octet) <= 255:
            return False, f"Octet '{octet}' is outside the range 0-255."
    return True, "Valid IP address format."


def generate_password():
    """
    Generate a strong random password of 10-16 characters containing
    uppercase, lowercase, digits and symbols. Uses the 'secrets' module,
    which is designed for cryptographic purposes (unlike 'random').
    """
    length = secrets.choice(range(10, 17))    # random length, 10 to 16 inclusive

    # Guarantee at least one character from every category
    characters = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    # Fill the remaining length from the full character pool
    pool = string.ascii_letters + string.digits + string.punctuation
    characters += [secrets.choice(pool) for _ in range(length - len(characters))]

    # Shuffle so the guaranteed characters are not always at the start
    secrets.SystemRandom().shuffle(characters)
    return "".join(characters)
