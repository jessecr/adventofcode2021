with open("input", "r") as fd:
    depths = [int(line) for line in fd if line]

# Part 1
num_increases = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        num_increases += 1

print(num_increases)

# Part 2
win_len = 3
num_increases = 0
for i in range(win_len + 1, len(depths) + 1):
    wina_start = i - win_len - 1
    wina_end = i - 1
    winb_start = i - win_len
    wina_sum = sum(depths[wina_start:wina_end])
    winb_sum = sum(depths[winb_start:i])
    if winb_sum > wina_sum:
        num_increases += 1

print(num_increases)
