# advanced_operations.py

import math

def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent

def square_root(x):
    """Return the square root of x. Raises ValueError if x is negative."""
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(x)