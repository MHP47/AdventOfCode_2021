from utils import *


def part_1(p_Input):
    diagram = defaultdict(lambda: 0)
    dat = [(parse_ints(y), parse_ints(z)) for y,z in [x.split(' -> ') for x in p_Input.splitlines()]]
    for (x1,y1),(x2,y2) in dat:
        if (x1 == x2):
            for i in range(min(y1,y2), max(y1,y2)+1):
                diagram[(x1,i)] += 1
        elif (y1 == y2):
            for i in range(min(x1,x2), max(x1, x2)+1):
                diagram[(i, y1)] += 1
    return len([x for x in list(diagram.values()) if x >= 2])


def part_2(p_Input):
    diagram = defaultdict(lambda: 0)
    dat = [parse_ints(x) for x in p_Input.splitlines()]
    for x1,y1,x2,y2 in dat:
        if (x1 == x2):
            for i in range(min(y1,y2), max(y1,y2)+1):
                diagram[(x1,i)] += 1
        elif (y1 == y2):
            for i in range(min(x1,x2), max(x1, x2)+1):
                diagram[(i, y1)] += 1
        else:
            if x1 > x2:
                x = range(x1, x2-1, -1)
                y = range(y1, y2+(1 if y2 > y1 else -1), 1 if y2 > y1 else -1)
            else:
                x = range(x2, x1-1, -1)
                y = range(y2, y1+(1 if y1 > y2 else -1), 1 if y1 > y2 else -1)

            for i,j in zip(x, y):
                diagram[(i,j)] += 1
    # print('  0123456789')
    # for y in range(10):
    #     print(f'{y} ', end='')
    #     for x in range(10):
    #         t = diagram[(x,y)]
    #         print('.' if t == 0 else t, end='')
    #     print()

    return len([x for x in list(diagram.values()) if x >= 2])


example_input_1 = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''
challenge_input = Input('5')

# assert(part_1(example_input_1) == 5)
# print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 12)
print(f"Part 2: {part_2(challenge_input)}")
