#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given non-negative integer recursively.

    Parameters:
    n (int): The non-negative integer to compute the factorial for.

    Returns:
    int: The computed factorial value of the integer n (returns 1 if n is 0).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Retrieve user argument, convert to int, and compute the factorial
f = factorial(int(sys.argv[1]))
print(f)
