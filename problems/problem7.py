"""
10001st prime
Problem 7
https://projecteuler.net/problem=7

By listing the first six prime numbers:
    2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from collections import deque
from typing import Deque


def get_n_primes(n_primes: int) -> Deque[int]:

    # queue because O(1) insertion time and O(n) iteration time.
    primes: Deque[int] = deque([2])

    # using a seperate var to track length as its ordinarily O(n) to check len
    # on a queue, with the var its O(0) to check len
    len_of_primes: int = 1

    n: int = 3  # int to check if prime

    while len_of_primes < n_primes:

        # if n is evenly divided by any prime, then its a not a prime
        if not any(map(lambda p: n % p == 0, primes)):  # the converse
            primes.append(n)
            len_of_primes += 1

        # since this iterates up "primes" will always have all factors of a
        # composite number being checked
        n += 1
    return primes


primes = get_n_primes(10_001)
print(primes.pop())
# answer: 104743
