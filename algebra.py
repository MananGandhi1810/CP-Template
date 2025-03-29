from functools import lru_cache


@lru_cache()
def binary_exponentiation(base: int, exponent: int, mod: int = None) -> int:
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")

    result = 1
    while exponent > 0:
        if exponent & 1:
            result = result * base if mod is None else (result * base) % mod
        base = base * base if mod is None else (base * base) % mod
        exponent >>= 1
    return result


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def fibonacci(n: int) -> int:
    """Iterative fibonacci calculation using dynamic programming"""
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
