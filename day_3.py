from utils import *
from collections import Counter


def part_1(p_Input):
    x = list(zip(*p_Input.splitlines()))
    gamma = epsilon = ''
    for i in x:
        mc = Counter(i).most_common()
        gamma += mc[0][0]
        epsilon += mc[1][0]
    return int(gamma,2) * int(epsilon,2)


def part_2(p_Input):
    x = p_Input.splitlines()
    itm_len = len(x[0])
    oxygen = co2 = x

    for i in range(itm_len):
        if len(oxygen) == len(co2) == 1:
            break

        if len(oxygen) > 1:
            mc = Counter(cat(list(zip(*oxygen))[i])).most_common()
            if mc[0][1] == mc[1][1]:
                mc_bit = '1'
            else:
                mc_bit = mc[0][0]
            oxygen = [z for z in oxygen if z[i] == mc_bit]

        if len(co2) > 1:
            mc = Counter(cat(list(zip(*co2))[i])).most_common()
            if mc[0][1] == mc[1][1]:
                mc_bit = '0'
            else:
                mc_bit = mc[1][0]
            co2 = [z for z in co2 if z[i] == mc_bit]
    
    return int(oxygen[0],2) * int(co2[0],2)

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

assert(part_2(example_input_1) == 230)
print(f"Part 2: {part_2(challenge_input)}")
