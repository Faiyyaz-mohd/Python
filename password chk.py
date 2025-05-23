import re

def is_strong_password(password):
    # Define the conditions for a strong password
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~" for char in password)
    is_long_enough = len(password) >= 8

    # Check all conditions
    if all([has_upper, has_lower, has_digit, has_special, is_long_enough]):
        return True
    return False

# Input password from the user
password = input("Enter a password to check if it's strong: ")

if is_strong_password(password):
    print("The password is strong.")
else:
    print("The password is weak. Make sure it has at least 8 characters, including uppercase, lowercase, digits, and special characters.")
