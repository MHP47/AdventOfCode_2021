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
    x = p_Input.splitlines()
    cnt = len(x)
    tmp = x
    oxygen = co2 = []


    y = [[a[i] for a in tmp] for i in range(len(tmp[0]))]
    for i in range(cnt):
        if len(tmp) == 1:
            break
        mc = Counter(cat(list(zip(y))[i][0])).most_common(2)
        if mc[0][1] == mc[1][1]:
            mc = '1'
        else:
            mc = mc[0][0]
        tmp = [z for z in tmp if z[i] == mc]
        y = [[a[i] for a in tmp] for i in range(len(tmp[0]))]

    oxygen = tmp[0]
    tmp = x
    y = [[a[i] for a in tmp] for i in range(len(tmp[0]))]

    for i in range(len(x)):
        if len(tmp) == 1:
            break
        mc = Counter(cat(list(zip(y))[i][0])).most_common()
        if mc[0][1] == mc[1][1]:
            mc = '0'
        else:
            mc = mc[1][0]
        tmp = [z for z in tmp if z[i] == mc]
        y = [[a[i] for a in tmp] for i in range(len(tmp[0]))]

    co2 = tmp[0]
    return int(oxygen,2) * int(co2,2)




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
