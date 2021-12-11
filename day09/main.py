from functools import reduce

input_file = "example_input"
input_file = "input"

array = [list(map(int, row.strip())) for row in open(input_file)]


def get_low_points(array):
    low_points = []
    num_rows = len(array)
    num_cols = len(array[0])
    for r in range(num_rows):
        for c in range(num_cols):
            val = array[r][c]
            if (
                (c == 0 or array[r][c - 1] > val)
                and (c == num_cols - 1 or array[r][c + 1] > val)
                and (r == 0 or array[r - 1][c] > val)
                and (r == num_rows - 1 or array[r + 1][c] > val)
            ):
                low_points.append((r, c))

    return low_points


def get_adjacent_cells(array, row, col):
    num_rows = len(array)
    num_cols = len(array[0])
    cells = []
    if row > 0:
        cells.append((row - 1, col))
    if row < num_rows - 1:
        cells.append((row + 1, col))
    if col > 0:
        cells.append((row, col - 1))
    if col < num_cols - 1:
        cells.append((row, col + 1))
    return cells


def explore_basin(array, cell, seen=None):
    if seen is None:
        seen = set([cell])
    r, c = cell
    val = array[r][c]
    basin = [cell]
    for next_cell in get_adjacent_cells(array, r, c):
        if next_cell in seen:
            continue

        next_val = array[next_cell[0]][next_cell[1]]

        if next_val == 9:
            continue

        if next_val > val:
            seen.add(next_cell)
            basin.extend(explore_basin(array, next_cell, seen))

    return basin


lows = get_low_points(array)
print("Part 1:", len(lows) + sum(array[r][c] for r, c in lows))

basins = []
for lowpoint in lows:
    basins.append(len(explore_basin(array, lowpoint)))

print("Part 2:", reduce(lambda x, y: x * y, sorted(b for b in basins)[-3:]))
