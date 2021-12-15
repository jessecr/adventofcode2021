from queue import PriorityQueue

import numpy as np

input_file = "example_input"
input_file = "input"

inp = open(input_file).read()
grid = np.array([list(map(int, row)) for row in inp.splitlines()])

adjacent_cell_offsets = ((0, 1), (0, -1), (1, 0), (-1, 0))


def get_adjacent_cells(shape, row, col):
    for ro, co in adjacent_cell_offsets:
        if 0 <= row + ro < shape[0] and 0 <= col + co < shape[1]:
            yield row + ro, col + co


def solve(num_grid_tiles):
    row = np.hstack([grid + i for i in range(num_grid_tiles)])
    costs = np.vstack([row + i for i in range(num_grid_tiles)])
    # 1-9 repeating
    mask = costs > 9
    costs[mask] = (costs[mask] - 1) % 9 + 1

    distances = np.ones(costs.shape) * np.inf
    distances[0][0] = 0

    visited = set()
    unvisited = PriorityQueue()
    unvisited.put((0, (0, 0)))
    while not unvisited.empty():
        p, cell = unvisited.get()
        for neighbor in get_adjacent_cells(costs.shape, cell[0], cell[1]):
            if neighbor not in visited:
                new_dist = distances[cell] + costs[neighbor]
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    unvisited.put((new_dist, neighbor))

        visited.add(cell)

    return int(distances[-1, -1])


print("Part 1:", solve(1))
print("Part 2:", solve(5))
