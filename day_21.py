import functools
from itertools import count
from utils import *


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def die_roll():
    x = itertools.cycle(range(1,101))
    while True:
        yield sum([next(x), next(x), next(x)])


def part_1(p_Input):
    players = dict(tuple(parse_ints(x)) for x in p_Input.splitlines())
    track = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    scores = { k: 0 for k in players.keys() }
    for p,roll in enumerate(die_roll()):
        player_id = (p%2)+1
        players[player_id] = (players[player_id] + roll)%10
        scores[player_id] += track[players[player_id]]
        if scores[player_id] >= 1000:
            loser_score = scores[((2-player_id)%2)+1]
            return loser_score * (p+1)*3


def part_2(p_Input):
    players = dict(tuple(parse_ints(x)) for x in p_Input.splitlines())
    rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    @functools.lru_cache(maxsize=None)
    def turn(player1, player2, player1_score=0, player2_score=0):
        if player2_score >= 21:
            return 0, 1
        p1_wins, p2_wins = 0, 0
        for k,v in rolls.items():
            loc = (player1 + k) % 10 or 10
            p2_wins_x, p1_wins_x = turn(player2, loc, player2_score, player1_score+loc)
            p1_wins, p2_wins = p1_wins + p1_wins_x*v, p2_wins + p2_wins_x*v
        return p1_wins, p2_wins

    return max(turn(*tuple(players.values())))


example_input_1 = '''Player 1 starting position: 4
Player 2 starting position: 8
'''
challenge_input = Input('21')

assert(part_1(example_input_1) == 739785)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 444356092776315)
assert(part_2(challenge_input) == 309196008717909)
print(f"Part 2: {part_2(challenge_input)}")
