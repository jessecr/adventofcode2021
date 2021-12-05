from collections import Counter
from itertools import chain, zip_longest

input_file = "example_input"
input_file = "input"

points = []
for line in open(input_file).readlines():
    points.append([int(p) for ax in line.split(' -> ') for p in ax.split(',')])

def coordinates(x1, y1, x2, y2, diagonals):
    if not diagonals and x1 != x2 and y1 != y2:
        return []
    fill = x2 if x1 == x2 else y2
    xd = 1 if x1 <= x2 else -1
    yd = 1 if y1 <= y2 else -1
    return list(zip_longest(range(x1, x2 + xd, xd), range(y1, y2 + yd, yd), fillvalue=fill))

def solve(diagonals):
    all_points = list(chain(*[coordinates(*point, diagonals) for point in points]))
    return len([cell for cell, count in Counter(all_points).items() if count > 1])

print(solve(diagonals=False))
print(solve(diagonals=True))
