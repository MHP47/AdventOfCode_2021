from utils import *


def part_1(p_Input):
    x1,x2,y1,y2 = parse_ints(p_Input)
    
    def step_calc(deltax, deltay):
        x_pos, y_pos = 0, 0
        y_max = 0
        while x_pos <= x2 and y1 <= y_pos:
            x_pos += deltax
            y_pos += deltay
            deltax = max(0, deltax-1)
            deltay -= 1
            y_max = max(y_max, y_pos)
            if x1<=x_pos<=x2 and y1<=y_pos<=y2:
                return y_max
        return -1

    y_limits = [z for z in [step_calc(x,y) for x in range(1,x2+1) for y in range(y1,-y1)] if z>= 0]
    return max(y_limits)

def part_2(p_Input):
    pass


example_input_1 = 'target area: x=20..30, y=-10..-5'
challenge_input = Input('17')

assert(part_1(example_input_1) == 45)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 'None')
print(f"Part 2: {part_2(challenge_input)}")
