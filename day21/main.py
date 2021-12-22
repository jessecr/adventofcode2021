from collections import Counter, defaultdict
from itertools import count, product


def part1(p1_pos, p2_pos):
    players = [[p1_pos, 0], [p2_pos, 0]]
    for i in count():
        n = 6 + (9 * i)
        player = players[i % 2]
        player[0] = (player[0] + n - 1) % 10 + 1
        player[1] += player[0]
        if player[1] >= 1000:
            break

    scores = [p[1] for p in players]
    rolls = (i + 1) * 3
    return min(scores) * rolls


def part2(p1_pos, p2_pos):
    roll_outcomes = Counter(sum(rolls) for rolls in product([1, 2, 3], repeat=3))
    states = defaultdict(int)
    # Mapping of (p1_position, p2_position, p1_score, p2_score) : num games with this state
    states[(p1_pos, p2_pos, 0, 0)] = 1
    wins = [0, 0]
    p = 0
    while states:
        updated_state = defaultdict(int)
        for game_state, player_count in states.items():
            pos = game_state[p]
            score = game_state[p + 2]
            for pos_offset, pos_count in roll_outcomes.items():
                new_pos = (pos + pos_offset - 1) % 10 + 1
                new_score = score + new_pos
                if new_score >= 21:
                    wins[p] += player_count * pos_count
                else:
                    if p == 0:
                        new_state = (new_pos, game_state[1], new_score, game_state[3])
                    else:
                        new_state = (game_state[0], new_pos, game_state[2], new_score)
                    updated_state[new_state] += player_count * pos_count
        states = updated_state
        p = (p + 1) % 2

    return max(wins)


p1_pos = 8
p2_pos = 5
print("Part 1:", part1(p1_pos, p2_pos))
print("Part 2:", part2(p1_pos, p2_pos))
