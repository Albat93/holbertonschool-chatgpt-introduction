#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input integer `n`. If `n` is 0, returns 1.
    """
    if n < 0:
        raise ValueError("The factorial is not defined for negative integers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Main script execution
if __name__ == "__main__":
    # Ensure the user provides exactly one argument
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)

    try:
        # Convert the command-line argument to an integer
        n = int(sys.argv[1])

        # Calculate the factorial of the given number
        f = factorial(n)

        # Print the calculated factorial
        print(f"The factorial of {n} is {f}")
    except ValueError as e:
        # Handle invalid input (non-integer or negative numbers)
        print(f"Error: {e}")
        sys.exit(1)
