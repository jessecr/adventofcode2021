from itertools import product

input_file = "example_input"
input_file = "input"

rows = [list(map(int, line)) for line in open(input_file).read().splitlines()]


def is_valid_cell(array, row, col):
    return row >= 0 and col >= 0 and row < len(array) and col < len(array[0])


adjacent_cell_offsets = list(product(*[range(-1, 2)] * 2))

all_cells = [(row, col) for row in range(len(rows)) for col in range(len(rows[0]))]
flashes = 0
i = 0
while True:
    i += 1
    for r, c in all_cells:
        rows[r][c] += 1

    to_flash = [(r, c) for r, c in all_cells if rows[r][c] > 9]
    while to_flash:
        for r, c in to_flash:
            rows[r][c] = -1
            for ro, co in adjacent_cell_offsets:
                r2 = r + ro
                c2 = c + co
                if is_valid_cell(rows, r2, c2) and rows[r2][c2] > -1:
                    rows[r2][c2] += 1
        to_flash = [(r, c) for r, c in all_cells if rows[r][c] > 9]

    for r, c in all_cells:
        if rows[r][c] == -1:
            flashes += 1
            rows[r][c] = 0

    if sum(map(sum, rows)) == 0:
        break

print(i)
print(flashes)
