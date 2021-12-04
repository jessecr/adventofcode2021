import math

input_file = "example_input"
input_file = "input"

chunks = open(input_file).read().split("\n\n")
nums = [int(n) for n in chunks[0].split(",")]
boards = [[int(n) for n in chunk.replace('\n', ' ').split()] for chunk in chunks[1:]]

board_width = int(math.sqrt(len(boards[0])))

def is_board_winning(board):
    for i in range(board_width):
        row_start = i * board_width
        if all(c is None for c in board[row_start:row_start + board_width]) or \
            all(c is None for c in board[i:len(board):board_width]):
            return True

    return False


def solve(win_cond):
    winning_boards = []
    for num in nums:
        for i, board in enumerate(boards):
            if i not in winning_boards and num in board:
                board[board.index(num)] = None
                if is_board_winning(board):
                    winning_boards.append(i)
        if win_cond(winning_boards):
            break

    board = boards[winning_boards[-1]]
    return num * sum([i for i in board if i is not None])

print(solve(lambda x: bool(x)))
print(solve(lambda x: len(x) == len(boards)))
