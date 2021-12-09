from utils import *


def part_1(p_Input):
    heightmap = defaultdict(lambda: 10)
    rows = p_Input.splitlines()
    for r in range(len(rows)):
        cols = list(map(int, list(rows[r])))
        for c in range(len(cols)):
            heightmap[(c,r)] = cols[c]
    count = 0
    for r in range(len(rows)):
        for c in range(len(cols)):
            p = heightmap[(c,r)]
            n = [heightmap[(x,y)] for x,y in neighbors4((c,r))]
            if all([p < x for x in n]):
                count += p+1
    return count

def part_2(p_Input):
    heightmap = defaultdict(lambda: 10)
    rows = p_Input.splitlines()
    for r in range(len(rows)):
        cols = list(map(int, list(rows[r])))
        for c in range(len(cols)):
            heightmap[(c,r)] = cols[c]
    lows = []
    for r in range(len(rows)):
        for c in range(len(cols)):
            p = heightmap[(c,r)]
            n = [heightmap[(x,y)] for x,y in neighbors4((c,r))]
            if all([p < x for x in n]):
                lows.append((c,r))
    sizes = []
    for c,r in lows:
        look = deque([(x,y) for x,y in neighbors4((c,r)) if heightmap[(x,y)] < 9 and heightmap[(c,r)] < heightmap[(x,y)]])
        size = 1
        seen = set()
        while look:
            a,b = look.popleft()
            seen.add((a,b))
            size+=1
            n = [(x,y) for x,y in neighbors4((a,b)) 
                 if heightmap[(x,y)] < 9 and heightmap[(a,b)] < heightmap[(x,y)]and (x,y) not in seen and (x,y) not in look]
            look.extend(n)
        sizes.append(size)
    
    return mul_reduce(sorted(sizes)[-3:])

example_input_1 = '''2199943210
3987894921
9856789892
8767896789
9899965678
'''
challenge_input = Input('9')

assert(part_1(example_input_1) == 15)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 1134)
print(f"Part 2: {part_2(challenge_input)}")
