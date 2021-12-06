from utils import *


def part_1(p_Input, days=80):
    fish = deque(parse_ints(p_Input))
    count = 0
    try:
        while f := fish.popleft():
            count += 1
            if f > days:
                continue
            fish.extend([x+1 for x in range(f+1,days+8,7)][1:])
    except IndexError:
        pass
    return count


def part_2(p_Input, p_Days=256):
    fish = deque([0]*9)
    for f in parse_ints(p_Input):
        fish[f] += 1
    for _ in range(p_Days):
        fish.rotate(-1)
        fish[6] += fish[8]
    return sum(fish)


example_input_1 = '3,4,3,1,2'
challenge_input = Input('6')

assert(part_1(example_input_1) == 5934)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 26984457539)
print(f"Part 2: {part_2(challenge_input)}")
