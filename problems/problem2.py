"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

previous_vals: tuple = (1, 2)  # first two terms as a seed
total = previous_vals[1]

for _ in range(2, 4_000_000):
    current_val = sum(previous_vals)  # n-th Fibonacci term

    if (current_val % 2 == 0):
        total += current_val

    if current_val > 4_000_000:
        break

    previous_vals = previous_vals[1], current_val  # cache previous_vals

print(total)