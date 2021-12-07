from utils import *
from statistics import median


def part_1(p_Input):
    coords = parse_ints(p_Input)
    dest = int(median(coords))
    return sum([abs(dest - x) for x in coords])


def part_2(p_Input):
    coords = parse_ints(p_Input)
    cmin, cmax = min(coords), max(coords)
    vals = []
    for dest in range(cmin, cmax):
        vals.append(sum([(y/2)*(1+y) for y in [abs(dest - x) for x in coords]]))
    return int(min(vals))


example_input_1 = '16,1,2,0,4,2,7,1,2,14'
challenge_input = Input('7')

assert(part_1(example_input_1) == 37)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 168)
print(f"Part 2: {part_2(challenge_input)}")
