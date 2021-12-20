import numpy as np

input_file = "example_input"
# input_file = "input"

algo, input_image = open(input_file).read().split('\n\n')

input_array = np.array(list(map(list[str], input_image.splitlines())))

def get_input_grid(input_array, center):
    row_slice = center[1] - 1, center[1] + 1
    col_slice = center[0] - 1, center[0] + 1
