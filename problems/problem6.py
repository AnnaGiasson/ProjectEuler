"""
Sum square difference
Problem 6
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is

    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

import operator
from functools import reduce

max_num: int = 100

sum_of_squares: int = sum(n*n for n in range(max_num + 1))
square_of_sum: int = reduce(operator.add, range(max_num + 1))**2

print(abs(sum_of_squares - square_of_sum))
# ans: 25164150
