from utils import *


def part_1(p_Input):
    cave = defaultdict(lambda: BIG)
    for y,dy in enumerate(p_Input.splitlines()):
        for x,dx in enumerate(dy):
            cave[(x,y)] = int(dx)
    dest_x, dest_y = x, y
    
    frontier = [(0, (0,0))]
    previous  = {(0,0): None}
    path_cost = {(0,0): 0}
    while frontier:
        (f, s) = heappop(frontier)
        if s == (dest_x, dest_y):
            break
        for tile in neighbors4(s):
            new_cost = path_cost[s] + cave[s]
            if tile not in path_cost or new_cost < path_cost[tile]:
                heappush(frontier, (new_cost, tile))
                path_cost[tile] = new_cost
                previous[tile] = s
    return sum([cave[x] for x in Path(previous, s)[1:]])
            

def part_2(p_Input):
    pass


example_input_1 = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
'''
challenge_input = Input('15')

assert(part_1(example_input_1) == 40)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 'None')
print(f"Part 2: {part_2(challenge_input)}")
