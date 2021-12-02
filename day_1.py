from utils import *


def part_1(p_Input):
    x = list(map(int, p_Input.splitlines()))
    return sum([x[i] > x[i-1] for i in range(1,len(x))])

def part_2(p_Input):
    x = list(map(int, p_Input.splitlines()))
    return sum([sum(x[i:i+3]) > sum(x[i-1:i+2]) for i in range(1,len(x)-2)])

example_input_1 = '''199
200
208
210
200
207
240
269
260
263
'''
challenge_input = Input('1')

assert(part_1(example_input_1) == 7)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 5)
print(f"Part 2: {part_2(challenge_input)}")
