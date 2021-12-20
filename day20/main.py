import numpy as np

input_file = "example_input"
input_file = "input"

algo, input_image = open(input_file).read().split("\n\n")

input_grid = np.array(list(map(list, input_image.splitlines())))


def expand_grid(grid, c, n=2):
    # Ensure there are `n` rows/columns of `c` as a border
    if not (grid[:, :n] == c).all():
        grid = np.hstack((np.array([c] * (grid.shape[0] * n)).reshape(-1, n), grid))
    if not (grid[:, -n:] == c).all():
        grid = np.hstack((grid, np.array([c] * (grid.shape[0] * n)).reshape(-1, n)))
    if not (grid[:n, :] == c).all():
        grid = np.vstack((np.array([c] * (grid.shape[1] * n)).reshape(n, -1), grid))
    if not (grid[-n:, :] == c).all():
        grid = np.vstack((grid, np.array([c] * (grid.shape[1] * n)).reshape(n, -1)))
    return grid


def get_sub_grid(input_grid, center):
    row_slice = center[0] - 1, center[0] + 2
    col_slice = center[1] - 1, center[1] + 2
    return input_grid[row_slice[0] : row_slice[1], col_slice[0] : col_slice[1]]


def get_output_image_character(input_grid, center):
    grid = get_sub_grid(input_grid, center)
    n = int("".join(grid.flatten()).replace(".", "0").replace("#", "1"), 2)
    return algo[n]


def generate_output_image(input_grid):
    output = []
    for r in range(1, input_grid.shape[0] - 1):
        row = []
        for c in range(1, input_grid.shape[1] - 1):
            row.append(get_output_image_character(input_grid, (r, c)))
        output.append(row)

    return np.array(output)


def get_empty_char(iteration, char_array):
    if char_array[0] == ".":
        return "."
    return ".#"[iteration % 2]


def get_num_light_pixels(input_grid, iterations):
    output = input_grid
    for i in range(iterations):
        output = generate_output_image(expand_grid(output, get_empty_char(i, algo)))

    return output.flatten().tolist().count("#")


print("Part 1:", get_num_light_pixels(input_grid, 2))
print("Part 2:", get_num_light_pixels(input_grid, 50))
