from utils import *
from collections import Counter


def part_1(p_Input):
    x = p_Input.splitlines()
    x = [[a[i] for a in x] for i in range(len(x[0]))]
    gamma = ''
    epsilon = ''
    for i in range(len(x)):
        a = x[i].count('0')
        b = x[i].count('1')
        gamma += '0' if a > b else '1'
        epsilon += '0' if a < b else '1'
    return int(gamma,2) * int(epsilon,2)



def part_2(p_Input):
    pass


example_input_1 = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''
challenge_input = Input('3')

assert(part_1(example_input_1) == 198)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 'None')
print(f"Part 2: {part_2(challenge_input)}")
