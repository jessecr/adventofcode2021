import operator

input_file = "example_input"
input_file = "input"

inp = open(input_file).read()

# inp = """inp z
# inp x
# mul z 3
# eql z x"""



def get_value_or_literal(values, v):
    if v in values:
        return values[v]
    return int(v)


cmds = {
    "add": operator.add,
    "mul": operator.mul,
    "mod": operator.mul,
    "div": operator.floordiv,
    "eql": operator.eq,
}

# for n in range(int(1e14) - 1, 0, -1):
#     if "0" in str(n):
#         continue
for n in range(111, 211):
    values = dict.fromkeys("wxyz", 0)
    if "0" in str(n):
        continue
    all_input = iter(str(n))
    for line in inp.splitlines():
        cmd, *args = line.split()
        if cmd == "inp":
            try:
                values[args[0]] = int(next(all_input))
            except StopIteration:
                break
        else:
            a, b = args
            values[a] = cmds[cmd](values[a], get_value_or_literal(values, b))

    print(n, values)

# print(values)

# def run(program, input_str, w=0, x=0, y=0, z=0):
#     input_iter = iter(input_str)
#     values = {"w": w, "x": x, "y": y, "z": z}
#     for line in program.splitlines():
#         cmd, *args = line.split()
#         if cmd == "inp":
#             values[args[0]] = int(next(input_iter))
#         else:
#             a, b = args
#             values[a] = cmds[cmd](values[a], get_value_or_literal(values, b))

#     return values

# print(run(inp[:inp.index('inp', 10)], '2'))
