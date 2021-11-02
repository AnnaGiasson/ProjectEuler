"""
Special Pythagorean triplet
Problem 9
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
#
# Since a, b, & c obey the Pythagorean theorm, then if c represents the
# hypotenuse of a right triangle and a & 2 thte two legs, c > (b & a). The
# other legs can then be relabels such that a is the smaller of the two (if not
# isosceles) an all inequalities will be met.

# The constraint, a + b + c = 1000, can then be used to eliminate one variable.
#   c = 1000 - a - b
#
# This can be usedd to produce the following relationship between a and b
#   a^2 + b^2 = c^2 = (1000 - a - b)^2 = 1000^2 - 1000a - 1000b
#                                       -1000a  + a^2   + ab
#                                       -1000b  + ab    + b^2
#   a^2 + b^2 = a^2 + 2ab + b^2 + 1000^2 - 2000a - 2000b
#           0 = 2ab + 1000^2 - 2000a - 2000b
#   -(2a - 2000)b = 1000^2 - 2000a
#               b = -(1000^2 - 2000a)/(2a - 2000)
#                 = -1000(500 - a)/(a - 1000)
#                 = 1000(a - 500)/(a - 1000)
#
# Since a & b must be natural numbers, and the sum a+b+c cann't exceed 1000,
# 0 < a < 334, to ensure b is positive.
# The Pythagorean triplet can then be found by doing a line search on the set
# of natural numbers for prospective values of "a" and checking that the
# equivalent value of "b" (from the above relationship) is also a natrual
# number.
# The Pythagorean theorm will then guarentee that "c" is a natual number.

from math import sqrt
from typing import Union


def solve_for_hypotenuse(leg1: int, leg2: int) -> Union[float, int]:
    return sqrt(leg1**2 + leg2**2)


def is_natural_number(num: Union[float, int]) -> bool:
    return (num > 0) and (num == int(num))


c = None

for a in range(1, 333):
    b = 1000*(a - 500)/(a - 1000)
    if is_natural_number(b):
        b = int(b)
        c = solve_for_hypotenuse(a, b)
        break

if c is None:
    raise Exception('Line search ended without a valid solution')
else:
    assert is_natural_number(c), 'c must be a natural number'
    c = int(c)

print(f'a = {a}, b = {b}, c = {c}',
      f'product = {a*b*c}', sep='\n')

# answer: 31875000
