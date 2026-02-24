"""
Program Name: User Login System
Author: Farouk Bellili
Purpose: This program simulates a login system using a dictionary to store
         usernames and passwords. It checks if the username exists and gives
         the user up to three attempts to enter the correct password. It then
         assigns a security level and greets the user.
Starter Code: None
Date: February 24, 2026
"""

# Dictionary with usernames and passwords
users = {
    "guest": "guest",
    "farouk": "python123",
    "admin": "securepass",
    "student": "cscc2026"
}

# Ask for username
username = input("Enter username: ")

# Check if username exists
if username not in users:
    print("User not found. Exiting.")

else:
    # Allow up to 3 password attempts
    attempts = 3

    while attempts > 0:
        password = input("Enter password: ")

        # Check if password is correct
        if password == users[username]:

            # Assign security level
            if username == "guest":
                security_level = "Guest access"
            else:
                security_level = "Security Level 1"

            print(f"\nWelcome, {username}. You have {security_level}.")
            break

        else:
            attempts -= 1

            if attempts == 0:
                print("Too many failed attempts. Account locked.")
            else:
                print(f"Access Denied. Attempts remaining: {attempts}")