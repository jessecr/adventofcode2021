def part_one(input_file: str) -> None:
    with open(input_file, "r") as fd:
        lines = fd.readlines()

    hpos = 0
    dpos = 0
    for line in lines:
        cmd, val = line.split()
        if cmd == "forward":
            hpos += int(val)
        elif cmd == "down":
            dpos += int(val)
        elif cmd == "up":
            dpos -= int(val)

    print(hpos * dpos)


def part_two(input_file: str) -> None:
    with open(input_file, "r") as fd:
        lines = fd.readlines()

    hpos = 0
    dpos = 0
    aim = 0
    for line in lines:
        parts = line.split()
        cmd = parts[0]
        val = int(parts[1])
        if cmd == "forward":
            hpos += val
            dpos += val * aim
        elif cmd == "down":
            aim += val
        elif cmd == "up":
            aim -= val

    print(hpos * dpos)


part_one("example_input")
part_one("input")

part_two("example_input")
part_two("input")
