import numpy as np

input_file = "example_input"
input_file = "input"

points_in, folds_in = open(input_file).read().split('\n\n')

folds = []
for line in folds_in.splitlines():
    axis, val_str = line.split()[-1].split('=')
    folds.append((axis, int(val_str)))

points = np.array([list(map(int, point.split(','))) for point in points_in.splitlines()])
grid = np.zeros((points[:, 1].max() + 1, points[:, 0].max() + 1)).astype(bool)
for x, y in points:
    grid[y][x] = True


def fold_it(grid, axis, fold_line):
    if axis == 'y':
        to_mirror = grid[fold_line + 1:]
        grid = grid[:fold_line]
        for x in range(len(to_mirror[0])):
            for y in range(len(to_mirror)):
                grid[fold_line - y - 1][x] |= to_mirror[y][x]
    elif axis == 'x':
        to_mirror = grid[:, fold_line + 1:]
        grid = grid[:, :fold_line]
        for y in range(len(to_mirror)):
            for x in range(len(to_mirror[0])):
                grid[y][fold_line - x - 1] |= to_mirror[y][x]

    return grid


print('Part 1:', fold_it(grid, folds[0][0], folds[0][1]).sum())

for fold in folds:
    grid = fold_it(grid, fold[0], fold[1])

print('Part 2')
for row in grid.astype(int):
    print(' '.join(map(str, row)).replace('0', '.').replace('1', 'x'))
