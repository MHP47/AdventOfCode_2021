from utils import *


def part_1(p_Input):
    fish = list(map(int, p_Input.split(',')))
    for _ in range(80):
        while True:
            try:
                idx = fish.index(0)
                fish[idx] = 7
                fish.append(9)
            except ValueError:
                break
        fish = [x-1 for x in fish]

    return len(fish)


def part_2(p_Input):
    pass


example_input_1 = '3,4,3,1,2'
challenge_input = Input('6')

assert(part_1(example_input_1) == 5934)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 'None')
print(f"Part 2: {part_2(challenge_input)}")
