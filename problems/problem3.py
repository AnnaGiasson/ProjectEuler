"""
Largest prime factor
Problem 3
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
from functools import lru_cache
from typing import Sequence


@lru_cache(maxsize=1024)
def is_prime(num: int) -> bool:
    for factor in range(2, math.ceil(math.sqrt(num))):
        if num % factor == 0:
            return False
    return True


def get_prime_factors(num: int) -> Sequence[int]:

    quotient: int = num
    for factor in range(2, math.ceil(math.sqrt(num)) + 1):
        if is_prime(factor):
            while quotient % factor == 0:
                yield factor
                quotient //= factor

    if is_prime(quotient):
        yield quotient


num: int = 600851475143
print(max(get_prime_factors(num)))
# answer: 6857
