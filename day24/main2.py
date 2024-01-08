from itertools import chain
import operator

input_file = "example_input"
input_file = "input"

inp = open(input_file).read()

# inp = """inp z
# inp x
# mul z 3
# eql z x"""

# values = dict.fromkeys("wxyz", 0)


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


def run(program, input_str, w=0, x=0, y=0, z=0):
    input_iter = iter(input_str)
    values = {"w": w, "x": x, "y": y, "z": z}
    for line in program:
        cmd, *args = line.split()
        if cmd == "inp":
            values[args[0]] = int(next(input_iter))
        else:
            a, b = args
            values[a] = cmds[cmd](values[a], get_value_or_literal(values, b))

    return values


inp_blocks = []
block = []
for line in inp.splitlines():
    if block and line.split()[0] == "inp":
        inp_blocks.append(block)
        block = []
    block.append(line)
inp_blocks.append(block)

# with open('output', 'w') as fd:
#     for i, block in enumerate(inp_blocks):
#         z_vals = range(26, 53) if i > 0 else [0]
#         for z in z_vals:
#             for v in range(1, 10):
#                 values = run(block, str(v), z=z)
#                 fd.write(f'Block: {i:< 2} input={v} zin={z:< 2} zout={values["z"]:< 2}\n')



# with open('output', 'w') as fd:
#     z_vals = [0]
#     for i, block in enumerate(inp_blocks):
#         new_z_vals = []
#         for z in z_vals:
#             for v in range(1, 10):
#                 values = run(block, str(v), z=z)
#                 fd.write(f'Block: {i:< 2} input={v} zin={z:< 2} zout={values["z"]:< 2}\n')
#                 new_z_vals.append(values['z'])

#         z_vals = new_z_vals


block = inp_blocks[-1]
s = 3118601829
e = 5688781085 + 1
d = (e - s) // 100
for z in range(s, e):
    if z % d == 0:
        print('%', ((z - s) // d) + 1)
    for v in range(1, 10):
        values = run(block, str(v), z=z)
        if values['z'] == 0:
            print(z, v)
            break


# for n in [1111111111111, 5555555555555, 9999999999999]:
#     values = run(chain(*inp_blocks[:-1]), str(n))
#     print(n, values)
#         # fd.write(f'Block: {i:< 2} input={v} zin={z:< 2} zout={values["z"]:< 2}\n')
