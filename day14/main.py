from collections import Counter

input_file = "example_input"
input_file = "input"

input_parts = open(input_file).read().split('\n\n')
insertions = {}
for cmd in input_parts[1].splitlines():
    match, insert = cmd.split(' -> ')
    insertions[match] = insert

polymer_template = input_parts[0].strip()


def solve(iterations):
    char_counts = Counter(polymer_template)
    pair_counts = {}
    for i in range(len(polymer_template) - 1):
        pair = polymer_template[i] + polymer_template[i + 1]
        pair_counts[pair] = pair_counts.get(pair, 0) + 1

    for _ in range(iterations):
        new_pairs = {}
        for pair, count in pair_counts.items():
            insert_char = insertions[pair]

            char_counts[insert_char] += count

            p1 = pair[0] + insert_char
            p2 = insert_char + pair[1]
            new_pairs[p1] = new_pairs.get(p1, 0) + count
            new_pairs[p2] = new_pairs.get(p2, 0) + count

        pair_counts = new_pairs

    mc = char_counts.most_common()
    return mc[0][1] - mc[-1][-1]


print('Part 1:', solve(10))
print('Part 2:', solve(40))
