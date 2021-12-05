from itertools import zip_longest

input_file = "example_input"
input_file = "input"

points = []
for line in open(input_file).readlines():
    points.append([int(p) for ax in line.split(' -> ') for p in ax.split(',')])

def solve(diagonals):
    cells = {}
    for x1, y1, x2, y2 in points:
        if not diagonals and x1 != x2 and y1 != y2:
            continue
        fill = x2 if x1 == x2 else y2
        xd = 1 if x1 <= x2 else -1
        yd = 1 if y1 <= y2 else -1
        for cell in list(zip_longest(range(x1, x2 + xd, xd), range(y1, y2 + yd, yd), fillvalue=fill)):
            cells[cell] = cells.get(cell, 0) + 1

    return len([cell for cell, count in cells.items() if count > 1])

print(solve(diagonals=False))
print(solve(diagonals=True))
