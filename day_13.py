from utils import *


def part_1(p_Input):
    dots, folds = p_Input.split('\n\n')
    dots = defaultdict(lambda: '.', {tuple(map(int,x.split(','))): '#' for x in dots.splitlines()})
    
    for f in folds.splitlines():
        if 'y=' in f:
            line = parse_ints(f)[0]
            for old,new in [((x,y),(x,line-y+line)) for x,y in dots.keys() if y > line]:
                del dots[old]
                dots[new] = '#'
        else:
            line = parse_ints(f)[0]
            for old,new in [((x,y),(line-x+line,y)) for x,y in dots.keys() if x > line]:
                del dots[old]
                dots[new] = '#'
        break
    return len(dots.keys())

def part_2(p_Input):
    dots, folds = p_Input.split('\n\n')
    dots = defaultdict(lambda: ' ', {tuple(map(int,x.split(','))): '#' for x in dots.splitlines()})
    
    for f in folds.splitlines():
        if 'y=' in f:
            line = parse_ints(f)[0]
            for old,new in [((x,y),(x,line-y+line)) for x,y in dots.keys() if y > line]:
                del dots[old]
                dots[new] = '#'
        else:
            line = parse_ints(f)[0]
            for old,new in [((x,y),(line-x+line,y)) for x,y in dots.keys() if x > line]:
                del dots[old]
                dots[new] = '#'

    return '\n'.join([cat([dots[(x,y)] for x in range((max(dots.keys(), key=lambda x: x[0]))[0]+1)]) for y in range(max(dots.keys(), key=lambda x: x[1])[1]+1)])

example_input_1 = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''
challenge_input = Input('13')

assert(part_1(example_input_1) == 17)
print(f"Part 1: {part_1(challenge_input)}")

print("Part 2:")
print(part_2(challenge_input))
