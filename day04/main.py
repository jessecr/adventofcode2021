import math

input_file = "day04/example_input"
# input_file = "input"
text = open(input_file, "r").read()

chunks = text.split("\n\n")
nums = [int(n) for n in chunks[0].split(",")]
boards = []
for chunk in chunks[1:]:
    boards.append([int(n) for n in " ".join(chunk.split()).split()])


def check_board(board):
    size = int(math.sqrt(len(board)))
    for r in range(size):
        if all(board[r : r + size]):
            print(board[r : r + size])
            return True
    for c in range(size):
        if all([board[i] for i in range(c, len(board), size)]):
            print([board[i] for i in range(c, len(board), size)])
            return True

    return False


hits = [[0] * len(board) for board in boards]
winner = None
for num in nums:
    for i, board in enumerate(boards):
        if num in board:
            idx = board.index(num)
            hits[i][idx] = 1

    for i, board in enumerate(hits):
        if check_board(board):
            print("hit", num)
            winner = i
            break

    if winner:
        break
else:
    print("no winner")
assert winner
hit = hits[winner]
board = boards[winner]
s = sum([board[i] for i, v in enumerate(hit) if not v])
print(s * num)


import math

input_file = "day04/example_input"
input_file = "day04/input"
text = open(input_file, "r").read()

chunks = text.split("\n\n")
nums = [int(n) for n in chunks[0].split(",")]
boards = []
for chunk in chunks[1:]:
    boards.append([int(n) for n in " ".join(chunk.split()).split()])


def check_board(board):
    size = int(math.sqrt(len(board)))
    for r in range(size):
        start = r * size
        if all(board[start : start + size]):
            return True
    for c in range(size):
        if all([board[i] for i in range(c, len(board), size)]):
            return True

    return False


hits = [[0] * len(board) for board in boards]
winner = None
wins = [False] * len(boards)
last = None
for num in nums:
    for i, board in enumerate(boards):
        if num in board:
            idx = board.index(num)
            hits[i][idx] = 1

    for i, board in enumerate(hits):
        if not wins[i] and check_board(board):
            wins[i] = True
            last = i

    if num == 13:
        print("13")

    if all(wins):
        break

print(num, last)
assert last
hit = hits[last]
board = boards[last]
s = sum([board[i] for i, v in enumerate(hit) if not v])
print(s, num)
print(s * num)

print(sorted([board[i] for i, v in enumerate(hit) if not v]))
print(sorted(map(int, "3 15 22 18 19 8 25 20 12 6".split())))
# print(sum(map(int, "3 15 22 18 19 8 25 20 12 6".split())))
