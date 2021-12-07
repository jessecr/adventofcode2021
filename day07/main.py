input_file = "example_input"
input_file = "input"

positions = [int(p) for p in open(input_file).read().split(",")]
part1 = {}
part2 = {}
for i in range(min(positions), max(positions) + 1):
    part1[i] = sum(abs(i - p) for p in positions)
    part2[i] = sum(int(abs(i - j) * (abs(i - j) + 1) / 2) for j in positions)

print(list(sorted(part1.items(), key=lambda x: x[1]))[0][1])
print(list(sorted(part2.items(), key=lambda x: x[1]))[0][1])
