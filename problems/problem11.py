"""
Largest product in a grid
Problem 11
https://projecteuler.net/problem=11

In the 20×20 grid below, four numbers along a diagonal line have been marked in
red [quotes].

08 02 22 97 38 15 00 40  00  75  04  05  07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57  60  87  17  40  98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29  93  71  40  67  53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42  69  24  68  56  01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89  41  92  36  54  22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02  44  75  33  53  78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 "26" 38  40  67  59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20  95 "63" 94  39  63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26  97  17 "78" 78  96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44  20  45  35 "14" 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67  15  94  03  80  04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47  55  58  88  24  00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07  05  44  44  37  44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69  28  73  92  13  86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16  07  97  57  32  16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72  03  46  33  67  46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11  24  94  72  18  08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88  34  62  99  69  82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01  74  31  49  71  48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69  16  92  33  48  61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?
"""

from functools import reduce
from itertools import chain
import operator
import re
from typing import Tuple


class NumTable:
    def __init__(self, text: str) -> None:
        self.table = tuple(self._generate_table(text))
        if len(self.table) == 0:
            raise ValueError('empty table')

        self.shape = (len(self.table), len(self.table[0]))

        is_rectangular = all(len(row) == self.shape[0] for row in self.table)
        if not is_rectangular:
            raise ValueError('table rows/columns must be of uniform legth')

    @staticmethod
    def _generate_table(text: str) -> Tuple[int]:

        digit_pattern = re.compile(r'\s?(\d\d)\s?')

        for row in text.split('\n'):
            if row == "":
                continue
            yield tuple(map(int, re.findall(digit_pattern, row)))

    def iter_rows(self, n_elems: int) -> Tuple[int]:
        for row in self.table:
            offset = 0
            while (offset + n_elems) <= self.shape[0]:
                yield row[offset:(offset + n_elems)]
                offset += 1

    def iter_columns(self, n_elems: int) -> Tuple[int]:

        for x in range(self.shape[1]):
            col = tuple(row[x] for row in self.table)

            offset = 0
            while (offset + n_elems) <= self.shape[0]:
                yield col[offset:(offset + n_elems)]
                offset += 1

    def iter_diagonals(self, n_elems: int) -> Tuple[int]:

        Y, X = self.shape
        starting_coords = chain(((0, y) for y in range(Y)),
                                ((x, 0) for x in range(1, X)))

        for coords in starting_coords:

            end_of_diagonal_reached = False
            while not end_of_diagonal_reached:
                x, y = coords

                try:
                    sequence: list[int] = []
                    for _ in range(n_elems):
                        sequence.append(self.table[y][x])
                        x, y = (x+1), (y+1)

                    yield tuple(sequence)
                    sequence.clear()
                    coords = (coords[0]+1), (coords[1]+1)

                except IndexError:
                    end_of_diagonal_reached = True

    def iter_reverse_diagonals(self, n_elems: int) -> Tuple[int]:

        Y, X = self.shape
        starting_coords = chain(((x, 0) for x in range(X-1)),
                                ((X-1, y) for y in range(Y)),
                                )

        for coords in starting_coords:

            end_of_diagonal_reached = False
            while not end_of_diagonal_reached:
                x, y = coords

                try:
                    sequence: list[int] = []
                    for _ in range(n_elems):
                        sequence.append(self.table[y][x])
                        x, y = (x-1), (y+1)

                    if x < -1:
                        # avoids negative indices NOT causing IndexError
                        break

                    yield tuple(sequence)

                    coords = (coords[0]-1), (coords[1]+1)

                except IndexError:
                    end_of_diagonal_reached = True


text_table = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

table = NumTable(text_table)
n_elems: int = 4

adjanct_numbers: Tuple[int] = chain(
                                    # table.iter_rows(n_elems),
                                    # table.iter_columns(n_elems),
                                    # table.iter_diagonals(n_elems),
                                    table.iter_reverse_diagonals(n_elems)
                                    )

max_prod: int = 0
for sequence in adjanct_numbers:
    prod = reduce(operator.mul, sequence)
    max_prod = max((prod, max_prod))

print(max_prod)
# answer: 70600674
