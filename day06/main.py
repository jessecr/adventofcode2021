input_file = "example_input"
input_file = "input"

fish = [int(f) for f in open(input_file).read().split(',')]

def solve(days):
    fish_age = [0] * 9
    for age in fish:
        fish_age[age] += 1
    for _ in range(days):
        fish_age = fish_age[1:] + [fish_age[0]]
        fish_age[6] += fish_age[8]

    return sum(fish_age)

print(solve(80))
print(solve(256))
