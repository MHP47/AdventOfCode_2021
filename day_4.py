from utils import *


def part_1(p_Input):
    numbers = list(map(int, p_Input.splitlines()[0].split(',')))
    bingo = defaultdict(list)
    boards_list = defaultdict(dict)
    boards = p_Input.splitlines()[2:]
    boards = [boards[x:x+5] for x in range(0, len(boards), 6)]
    for b in range(len(boards)):
        l = len(boards[b][0].split())
        for r in range(l):
            boards_list[b][r] = []
            for i,n in enumerate(parse_ints(boards[b][r])):
                bingo[n].append((b, r, i))
                boards_list[b][r].append(n)

    def check_complete(p_board):
        for b,brd in p_board.items():
            # Check rows
            for r,nums in brd.items():
                if all([isinstance(x, bool) for x in nums]):
                    return b
            # Check cols
            for nums in list(zip(*list(brd.values()))):
                if all([isinstance(x, bool) for x in nums]):
                    return b
        return None

    for n in numbers:
        for b,r,i in bingo[n]:
            boards_list[b][r][i] = True
        winner = check_complete(boards_list)
        if isinstance(winner, int):
            break
    count = 0
    for _,nums in boards_list[winner].items():
        count += sum([x for x in nums if not isinstance(x, bool)])
    return count * n


def part_2(p_Input):
    numbers = list(map(int, p_Input.splitlines()[0].split(',')))
    bingo = defaultdict(list)
    boards_list = defaultdict(dict)
    boards = p_Input.splitlines()[2:]
    boards = [boards[x:x+5] for x in range(0, len(boards), 6)]
    for b in range(len(boards)):
        l = len(boards[b][0].split())
        for r in range(l):
            boards_list[b][r] = []
            for i,n in enumerate(parse_ints(boards[b][r])):
                bingo[n].append((b, r, i))
                boards_list[b][r].append(n)

    boards_list = dict(boards_list)

    def check_complete(p_board):
        ret = set()
        for b,brd in p_board.items():
            # Check rows
            for r,nums in brd.items():
                if all([isinstance(x, bool) for x in nums]):
                    ret.add(b)
            # Check cols
            for nums in list(zip(*list(brd.values()))):
                if all([isinstance(x, bool) for x in nums]):
                    ret.add(b)
        return None if not ret else ret

    for n in numbers:
        for b,r,i in bingo[n]:
            try:
                boards_list[b][r][i] = True
            except KeyError:
                pass
        winner = check_complete(boards_list)
        if isinstance(winner, set):
            if len(boards_list.values()) == 1:
                break
            for i in winner:
                del boards_list[i]
    count = 0
    for _,nums in list(boards_list.values())[0].items():
        count += sum([x for x in nums if not isinstance(x, bool)])
    return count * n


example_input_1 = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''
challenge_input = Input('4')

assert(part_1(example_input_1) == 4512)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 1924)
print(f"Part 2: {part_2(challenge_input)}")
