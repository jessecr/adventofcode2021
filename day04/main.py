from collections import OrderedDict
from math import sqrt

input_file = "example_input"
input_file = "input"

chunks = open(input_file).read().split("\n\n")
nums = [int(n) for n in chunks[0].split(",")]
boards = [[int(n) for n in chunk.replace('\n', ' ').split()] for chunk in chunks[1:]]

board_width = int(sqrt(len(boards[0])))

def get_rows(board, axis):
    if not axis:  # rows
        return [board[i * board_width:(i * board_width) + board_width] for i in range(board_width)]
    return [board[i:len(board):board_width] for i in range(board_width)]

won = OrderedDict()
for selected in (nums[:i] for i in range(1, len(nums))):
    for bi, board in enumerate(boards):
        if bi not in won and any(set(r).issubset(selected) for r in get_rows(board, 0) + get_rows(board, 1)):
            won[bi] = sum(set(board).difference(selected)) * selected[-1]

winners = list(won.items())
print(winners[0][1])
print(winners[-1][1])
