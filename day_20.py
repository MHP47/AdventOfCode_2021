from utils import *


def enhance(pixel_set, step_number, algorithm):
    x_min, x_max = min(pixel_set, key=lambda n: n[0])[0], max(pixel_set, key=lambda n: n[0])[0]
    y_min, y_max = min(pixel_set, key=lambda n: n[1])[1], max(pixel_set, key=lambda n: n[1])[1]
    lights = set()
    
    for y in range(y_min - 3, y_max + 4):
        for x in range(x_min - 3, x_max + 4):
            key = int(cat([str(step_number%2) if not (y_min<=dy<=y_max and x_min<=dx<=x_max) else '1' if (dx,dy) in pixel_set else '0'
                        for dy in range(y-1,y+2) for dx in range(x-1,x+2)]), 2)
            if algorithm[key] == '#':
                lights.add((x,y))
    
    return lights


def part_1(p_Input):
    iea, img = p_Input.split('\n\n')
    light_pixels = set()
    for y,r in enumerate(img.splitlines()):
        for x,c in enumerate(r):
            if c == '#':
                light_pixels.add((x,y))
    
    for step in range(2):
        light_pixels = enhance(light_pixels, step, iea)
    return len(light_pixels)

def part_2(p_Input):
    pass


example_input_1 = '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
'''
challenge_input = Input('20')

# assert(part_1(example_input_1) == 35)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 'None')
print(f"Part 2: {part_2(challenge_input)}")
