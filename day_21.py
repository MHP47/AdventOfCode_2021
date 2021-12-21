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
    pass


example_input_1 = '''Player 1 starting position: 4
Player 2 starting position: 8
'''
challenge_input = Input('21')

assert(part_1(example_input_1) == 739785)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 'None')
print(f"Part 2: {part_2(challenge_input)}")
