def divide(a, b):
    """Divide a by b, raising an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n):
    """Return the factorial of n, an exact integer >= 0."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    if n == 0:
        return 1
    return n * factorial(n-1)
