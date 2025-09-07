"""
This script demonstrates basic Python functions:
- greet a user
- compute factorial of a number
- generate a Fibonacci series
- check if a number is prime

It is used for practicing Git, GitHub, and pylint workflows.
"""
# This is a test to trigger GitHub Actions

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def factorial(n):
    """Return factorial of n using recursion."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Return Fibonacci sequence up to n terms."""
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(greet("World"))
    print("Factorial of 5:", factorial(5))
    print("Fibonacci (10 terms):", fibonacci(10))
    print("Prime check for 29:", is_prime(29))
