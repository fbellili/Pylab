"""
Program Name: UPC Validator
Author: Farouk Bellili
Purpose: This program checks if a 12-digit UPC code is valid. It asks the user
         for a UPC number, calculates the expected check digit using a function,
         and compares it with the provided check digit to determine if the UPC
         is valid.
Starter Code: None
Date: March 10, 2026
"""

def find_UPC(first11):
    # Convert digits to int
    digits = [int(d) for d in first11]

    # Sum of digits in odd positions
    odd_sum = digits[0] + digits[2] + digits[4] + digits[6] + digits[8] + digits[10]

    # Sum of digits in even positions
    even_sum = digits[1] + digits[3] + digits[5] + digits[7] + digits[9]

    # Multiply odd sum by 3
    total = (odd_sum * 3) + even_sum

    # Calculate check digit
    check_digit = (10 - (total % 10)) % 10

    return check_digit



while True:
    upc = input("Enter a 12-digit UPC: ")

    if len(upc) != 12 or not upc.isdigit():
        print("Error: UPC must be exactly 12 digits. Please try again.\n")
    else:
        break


first11 = upc[:11]
provided_digit = int(upc[11])

print()
print(f"The first 11 digits are '{first11}'.")
print(f"The provided check digit is '{provided_digit}'.")
print()
print("Calculating...")

expected_digit = find_UPC(first11)

print(f"The expected check digit is {expected_digit}.")
print()

if expected_digit == provided_digit:
    print("This is a VALID UPC.")
else:
    print("This is an INVALID UPC.")
