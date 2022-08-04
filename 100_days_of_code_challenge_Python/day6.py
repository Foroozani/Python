"""
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""

def sum_two_integer(a, b):
    total = a + b
    if total > 15 and total < 20:
        return 20
    else:
        return total

sum_two_integer(10, 6)