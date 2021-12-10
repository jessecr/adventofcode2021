input_file = "example_input"
input_file = "input"

open_to_closing_chars = {"{": "}", "(": ")", "[": "]", "<": ">"}
illegal_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
ac_points = {")": 1, "]": 2, "}": 3, ">": 4}

illegal_score = 0
ac_scores = []

for line in open(input_file):
    expected_closing_chars = []
    for c in line.strip():
        if c in open_to_closing_chars:
            expected_closing_chars.append(open_to_closing_chars[c])
        elif c != expected_closing_chars.pop():
            illegal_score += illegal_points[c]
            break
    else:
        if expected_closing_chars:
            total = 0
            for c in expected_closing_chars[::-1]:
                total = (total * 5) + ac_points[c]
            ac_scores.append(total)

print(illegal_score)
print(sorted(ac_scores)[len(ac_scores) // 2])
