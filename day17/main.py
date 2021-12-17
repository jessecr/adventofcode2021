import re

inp = "target area: x=20..30, y=-10..-5"
inp = "target area: x=111..161, y=-154..-101"

match = re.search("x=(-?\d+)\.\.(-?\d+), y=(-?\d+)..(-?\d+)", inp)
assert match
x1, x2, y1, y2 = map(int, match.groups())
x_target_min, x_target_max = sorted([x1, x2])
y_target_min, y_target_max = sorted([y1, y2])


def simulate(x_vel, y_vel):
    x = 0
    y = 0
    max_y = 0
    while x < x_target_max and y > y_target_min:
        x += x_vel
        y += y_vel
        max_y = max(max_y, y)
        x_vel = max(x_vel - 1, 0)
        y_vel -= 1

        if x_target_min <= x <= x_target_max and y_target_min <= y <= y_target_max:
            return max_y

    return None


max_height = max(simulate(x, y) or 0 for x in range(200) for y in range(200))
print("Part 1:", max_height)

total_hits = sum(simulate(x, y) is not None for x in range(200) for y in range(-200, 200))
print("Part 2:", total_hits)
