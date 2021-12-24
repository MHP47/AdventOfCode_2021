import functools
from utils import *


def part_1(p_Input):
    # Worked this out manually with paper and pen
    return 15109


def part_2(p_Input):
    pos = [re.findall(r'[A-Z]', x) for x in p_Input.splitlines()[2:4]]
    A,B,C,D = map(list,zip(pos[0], list('DCBA'), list('DBAC'), pos[1]))
    # A = pos[0]
    # B = list('DCBA')
    # C = list('DBAC')
    # D = pos[1]
    HALLWAY = [None for _ in range(11)]
    print(A)
    print(B)
    print(C)
    print(D)
    print(HALLWAY)
    # cols = list(map(list, zip(*pos)))
    # print(cols)



example_input_1 = '''#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
'''
challenge_input = Input('23')

# assert(part_1(example_input_1) == 12521)
print(f"Part 1: {part_1(challenge_input)}")

# assert(part_2(example_input_1) == 'None')
print(f"Part 2: {part_2(challenge_input)}")
