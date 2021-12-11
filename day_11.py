from utils import *


def part_1(p_Input, p_Steps=100):
    octo = defaultdict(int)
    octo = dict()
    total = 0
    for rows, x in enumerate(p_Input.splitlines()):
        for cols, y in enumerate(map(int, list(x))):
            octo[(cols,rows)] = y

    for step in range(1, p_Steps+1):
        flashed = set()
        proc = deque()
        for i in octo.keys():
            octo[i] += 1
            if octo[i] > 9:
                proc.append(i)

        while proc:
            pass
            n = proc.popleft()
            flashed.add(n)
            for x in neighbors8(n):
                if 0 <= X(x) <= cols and 0 <= Y(x) <= rows:
                    if x not in flashed:
                        octo[x] += 1
                        if octo[x] > 9 and x not in proc:
                            proc.append(x)
        for n in flashed:
            octo[n] = 0

        total += len(flashed)
    
    print(total)
    return total


def part_2(p_Input):
    pass


example_input_1 = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''
example_input_2 = '''11111
19991
19191
19991
11111
'''
challenge_input = Input('11')

assert(part_1(example_input_2, 2) == 9)
assert(part_1(example_input_1, 100) == 1656)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
