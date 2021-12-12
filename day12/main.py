from collections import defaultdict

input_file = "example_input"
input_file = "input"


def traverse(path: list[str], all_paths: list[list[str]], revisited_small_cave=False):
    cave = path[-1]
    if cave == "end":
        all_paths.append(path)
        return
    for next_cave in cave_connections[cave]:
        if next_cave.isupper() or next_cave not in path:
            traverse(path + [next_cave], all_paths, revisited_small_cave=revisited_small_cave)
        elif next_cave != "start" and not revisited_small_cave:
            traverse(path + [next_cave], all_paths, revisited_small_cave=True)


cave_connections: dict[str, list[str]] = defaultdict(list)
for line in open(input_file).read().splitlines():
    a, b = line.split("-")
    cave_connections[a].append(b)
    cave_connections[b].append(a)

part_one_paths: list[list[str]] = []
traverse(["start"], part_one_paths, revisited_small_cave=True)
print("Part 1:", len(part_one_paths))

part_two_paths: list[list[str]] = []
traverse(["start"], part_two_paths)
print("Part 2:", len(part_two_paths))
