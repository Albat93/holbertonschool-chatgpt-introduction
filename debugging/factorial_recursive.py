#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    It is denoted as n! and defined as:
    - 0! = 1 (by definition)
    - n! = n * (n-1)! for n > 0

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the integer n. If n is 0, the function returns 1 as per the definition of factorial.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the input value from the command line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
