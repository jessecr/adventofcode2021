input_file = "example_input"
input_file = "input"


def part_one():
    s = 0
    for line in open(input_file):
        _, o = line.split("|")
        uq = [v for v in o.strip().split() if len(v) in (2, 3, 4, 7)]
        s += len(uq)

    return s


def part_two():
    def solve_line(line):
        i, o = line.split("|")
        input_signals = i.strip().split()
        output_signals = o.strip().split()

        lengths = {}
        for signal in input_signals:
            lengths.setdefault(len(signal), []).append(signal)

        one = set(lengths[2][0])
        four = set(lengths[4][0])
        seven = set(lengths[3][0])
        eight = set(lengths[7][0])

        signal_and_digit = [
            (one, 1),
            (four, 4),
            (seven, 7),
            (eight, 8),
        ]
        for signal in input_signals:
            if len(signal) == 5:
                if len(one.intersection(signal)) == 2:
                    signal_and_digit.append((set(signal), 3))
                elif len(four.difference(one).intersection(signal)) == 2:
                    signal_and_digit.append((set(signal), 5))
                else:
                    signal_and_digit.append((set(signal), 2))
            elif len(signal) == 6:
                if len(eight.difference(one).intersection(signal)) == 5:
                    signal_and_digit.append((set(signal), 6))
                elif len(four.intersection(signal)) == 4:
                    signal_and_digit.append((set(signal), 9))
                else:
                    signal_and_digit.append((set(signal), 0))

        output_digits = []
        for output_signal in output_signals:
            for signal, digit in signal_and_digit:
                if signal == set(output_signal):
                    output_digits.append(digit)
                    break

        return int("".join(map(str, output_digits)))

    vals = []
    for line in open(input_file):
        vals.append(solve_line(line))

    return sum(vals)


print(part_one())
print(part_two())
