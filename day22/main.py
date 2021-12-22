import re

input_file = "example_input"
input_file = "input"

inp = open(input_file).read()


def get_cube_area(x1, x2, y1, y2, z1, z2):
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)


def get_intersection(ax1, ax2, ay1, ay2, az1, az2, bx1, bx2, by1, by2, bz1, bz2):
    x3 = max(ax1, bx1)
    y3 = max(ay1, by1)
    z3 = max(az1, bz1)
    x4 = min(ax2, bx2)
    y4 = min(ay2, by2)
    z4 = min(az2, bz2)
    intersects = x3 <= x4 and y3 <= y4 and z3 <= z4
    return intersects, (x3, x4, y3, y4, z3, z4) if intersects else None


def solve(all_cube_coords):
    """
    For each new cube, check for intersections with every cube we have already seen. If there is
    an intersection add the intersection cube to the "off" cubes list.
    The idea here is to not double count the overlapping area of two "on" cubes.

    Then check that new cube for intersections with every "off" cube we have added. If there
    is an intersection, add the intersection of those two cubes into the "on" cubes list.
    The idea here is to not double count "off" cubes, which we offset by adding their overlap back
    as an "on" cube.

    Finally subtract the area of the "off" cubes from the "on" cubes.

    I'm sure there's a way to combine these steps and only perform one loop, but this works and
    isn't too slow.
    """

    cubes = []
    intersections = []
    for action, new_cube_coords in all_cube_coords:
        ix_update = []
        for existing_cube_coords in cubes:
            intersects, ix_coords = get_intersection(*new_cube_coords, *existing_cube_coords)
            if intersects:
                ix_update.append(ix_coords)

        cube_update = []
        for ix_cube_coords in intersections:
            intersects, ix_coords = get_intersection(*new_cube_coords, *ix_cube_coords)
            if intersects:
                cube_update.append(ix_coords)

        if action == "on":
            cube_update.append(new_cube_coords)
        cubes.extend(cube_update)
        intersections.extend(ix_update)

    on_area = sum(get_cube_area(*coords) for coords in cubes)
    off_area = sum(get_cube_area(*coords) for coords in intersections)
    return on_area - off_area


all_cubes = []
for line in inp.splitlines():
    action, rest = line.split()
    new_cube_coords = list(map(int, re.findall("-?\d+", rest)))
    all_cubes.append((action, new_cube_coords))

part1_cubes = [v for v in all_cubes if abs(v[1][0]) <= 50]

print("Part 1:", solve(part1_cubes))
print("Part 2:", solve(all_cubes))
