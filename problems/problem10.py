"""
Summation of primes
Problem 10
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# More efficient prime number generators
#
# Sieves:
# https://en.wikipedia.org/wiki/Sieve_of_Atkin
#
# Primality proving methods
# https://en.wikipedia.org/wiki/Elliptic_curve_primality
# https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test

# Once a method is chosen pick an appropreiate data structure.

from typing import List


def sieve_eratosthenes(n_max: int) -> List[int]:
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    primes: List[int] = []

    if n_max < 2:
        return primes

    # list of int, flagged as prime by default
    domain = [True]*n_max
    domain[0:2] = (False, False)  # 0 and 1 are not prime

    for n, is_prime in enumerate(domain):
        if not is_prime:
            continue
        primes.append(n)

        # flag multiples as not prime
        for idx in range(n, n_max, n):
            domain[idx] = False

    return primes


primes = sieve_eratosthenes(2_000_000)
print(sum(primes))
# ans: 142913828922
