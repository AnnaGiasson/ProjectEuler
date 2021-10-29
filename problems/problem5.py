"""
Smallest multiple
Problem 5
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import math
from functools import lru_cache, reduce
from typing import Dict, Generator


@lru_cache(maxsize=1024)
def is_prime(num: int) -> bool:
    for factor in range(2, math.ceil(math.sqrt(num))):
        if num % factor == 0:
            return False

    return (num != 1)


def iterate_prime_factors(num: int) -> Generator[int, int, None]:

    quotient: int = num
    for factor in range(2, math.ceil(math.sqrt(num)) + 1):
        if is_prime(factor):
            while quotient % factor == 0:
                yield factor
                quotient //= factor

    if is_prime(quotient):
        yield quotient


def get_factor_tree(num: int) -> Dict[int, int]:
    """
    keys = prime factors
    values = multiplicity
    """

    factor_tree: Dict[int, int] = {}

    for factor in iterate_prime_factors(num):
        factor_tree[factor] = factor_tree.get(factor, 0) + 1

    return factor_tree


def reduce_factor_tree(tree: Dict[int, int]) -> int:
    return reduce(lambda a, b: a*b,
                  (prime**mult for prime, mult in tree.items()))


# if a integer is divisable by every member in a set of integers then its
# factor tree will be a super-set of the factor tree of each integer in the set

# the smallest number that meets this criteria will have a factor tree that
# has the unique set of factors present in all factor trees within the set.
# The multiplicity of each factor in its tree will be equal to the max
# multiplicity of that factor in all factor trees within the set in question.


ans_factor_tree: Dict[int, int] = {}
for num in range(2, 21):

    tree = get_factor_tree(num)

    for factor, multiplicity in tree.items():

        # build the factor tree up such that it contains
        ans_factor_tree[factor] = max((ans_factor_tree.get(factor, 0),
                                       multiplicity))


print(reduce_factor_tree(ans_factor_tree))
# answer: 232792560
