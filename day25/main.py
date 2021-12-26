input_file = "example_input"
input_file = "input"

inp = open(input_file).read()

grid = [list(line) for line in inp.splitlines()]

num_rows = len(grid)
num_cols = len(grid[0])
moved = True
i = 0
while moved:
    moved = False
    for shape, offset in (('>', (0, 1)), ('v', (1, 0))):
        to_move = []
        for r in range(num_rows):
            for c in range(num_cols):
                next_row = (r + offset[0]) % num_rows
                next_col = (c + offset[1]) % num_cols
                if grid[r][c] == shape and grid[next_row][next_col] == '.':
                    to_move.append((r, c, next_row, next_col))

        for r1, c1, r2, c2 in to_move:
            grid[r1][c1] = '.'
            grid[r2][c2] = shape

        if to_move:
            moved = True

    i += 1

print(i)
