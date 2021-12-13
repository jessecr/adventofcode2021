import numpy as np

input_file = "example_input"
input_file = "input"

points_in, folds_in = open(input_file).read().split('\n\n')

folds = []
for line in folds_in.splitlines():
    axis, val_str = line.split()[-1].split('=')
    folds.append((axis, int(val_str)))

height = max(val for ax, val in folds if ax == 'y') * 2 + 1
width = max(val for ax, val in folds if ax == 'x') * 2 + 1

points = [list(map(int, point.split(','))) for point in points_in.splitlines()]
grid = np.zeros((height, width))
for x, y in points:
    grid[y][x] = 1


def fold_it(grid, axis, val):
    if axis == 'y':
        to_mirror = grid[val + 1:][::-1]
        grid = grid[:val]
    elif axis == 'x':
        to_mirror = grid[:, val + 1:][:, ::-1]
        grid = grid[:, :val]

    return np.logical_or(grid, to_mirror).astype(int)


print('Part 1:', fold_it(grid, folds[0][0], folds[0][1]).sum())

for fold in folds:
    grid = fold_it(grid, fold[0], fold[1])

print('Part 2')
for row in grid.astype(int):
    print(' '.join(map(str, row)).replace('0', '.').replace('1', 'x'))
