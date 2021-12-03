import numpy as np

input_file = "example_input"
input_file = "input"

nums = open(input_file).read().splitlines()
bits = len(nums[0])
arr = np.array([list(map(int, x)) for x in nums])

# Part 1
gamma_bits = [np.argmax(bc) for bc in np.apply_along_axis(np.bincount, 1, arr.T)]
gamma = sum(v << i for i, v in enumerate(gamma_bits[::-1]))
eps = ~gamma & 2 ** bits - 1

print(f"Part 1: {eps * gamma}")


# Part 2
def doit(bit_f):
    arr2 = arr
    col = 0
    while len(arr2) > 1:
        bins = np.bincount(arr2[:, col])
        thebit = bit_f(bins[0], bins[1])
        idxs = (arr2[:, col] == thebit).nonzero()[0]
        arr2 = arr2[idxs, :]
        col += 1
    return sum(v << i for i, v in enumerate(arr2[0, :][::-1]))


o2 = doit(lambda x, y: 1 if x <= y else 0)
co2 = doit(lambda x, y: 0 if x <= y else 1)

print(f"Part 2: {co2 * o2}")
