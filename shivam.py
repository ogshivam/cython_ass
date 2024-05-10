def factorial(n: int) -> int:
    """
    Vanilla Python function to calculate the factorial of a given number.
    """
    result: int = 1
    for i in range(1, n + 1):
        result *= i
    return result
