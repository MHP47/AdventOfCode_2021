from utils import *


def part_1(p_Input):
    horiz = 0
    depth = 0
    comms = [x.split() for x in p_Input.splitlines()]
    for h,d in comms:
        if h == 'forward':
            horiz += int(d)
        elif h == 'down':
            depth += int(d)
        elif h == 'up':
            depth -= int(d)
        else:
            raise
    return horiz * depth


def part_2(p_Input):
    horiz = 0
    depth = 0
    aim = 0
    comms = [x.split() for x in p_Input.splitlines()]
    for h,d in comms:
        if h == 'forward':
            horiz += int(d)
            depth += int(d)*aim
        elif h == 'down':
            aim += int(d)
        elif h == 'up':
            aim -= int(d)
        else:
            raise
    return horiz * depth


example_input_1 = '''forward 5
down 5
forward 8
up 3
down 8
forward 2
'''
challenge_input = Input('2')

assert(part_1(example_input_1) == 150)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 900)
print(f"Part 2: {part_2(challenge_input)}")
