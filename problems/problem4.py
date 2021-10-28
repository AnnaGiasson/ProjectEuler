"""
Largest palindrome product
Problem 4
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools


def is_palindrome_number(num: int) -> bool:
    num_str = str(num)
    return num_str == num_str[::-1]


max_prod: int = 0

for x, y in itertools.product(range(100, 1000), range(100, 1000)):
    current_prod = x*y

    if is_palindrome_number(current_prod) and (current_prod > max_prod):
        max_prod = current_prod

print(max_prod)
# answer: 906609
