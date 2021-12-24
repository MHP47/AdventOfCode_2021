from utils import *


def part_1(p_Input):
    commands_list = p_Input.split('inp w\n')[1:]
    # The only lines that differ between each group are 3, 4 and 14
    z = []
    model = [0] * 14
    for i,c in enumerate(commands_list):
        cmds = c.splitlines()
        x_add = int(cmds[4].split()[-1])
        y_add = int(cmds[14].split()[-1])
        if cmds[3] == 'div z 1':
            z.append((i, y_add))
        elif cmds[3] == 'div z 26':
            j, tmp = z.pop()
            tmp += x_add
            model[i] = 9 + tmp if tmp < 0 else 9
            model[j] = 9 - tmp if tmp > 0 else 9

    return cat(map(str, model))

def part_2(p_Input):
    commands_list = p_Input.split('inp w\n')[1:]
    # The only lines that differ between each group are 3, 4 and 14
    z = []
    model = [0] * 14
    for i,c in enumerate(commands_list):
        cmds = c.splitlines()
        x_add = int(cmds[4].split()[-1])
        y_add = int(cmds[14].split()[-1])
        if cmds[3] == 'div z 1':
            z.append((i, y_add))
        elif cmds[3] == 'div z 26':
            j, tmp = z.pop()
            tmp += x_add
            model[i] = 1 + tmp if tmp > 0 else 1
            model[j] = 1 - tmp if tmp < 0 else 1

    return cat(map(str, model))


example_input_1 = '''inp x
mul x -1
'''
example_input_2 = '''inp z
inp x
mul z 3
eql z x
'''
example_input_3 = '''inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
'''
challenge_input = Input('24')
if __name__ == '__main__':
    # assert(part_1(example_input_2) == 'None')
    print(f"Part 1: {part_1(challenge_input)}")

    # assert(part_2(example_input_1) == 'None')
    print(f"Part 2: {part_2(challenge_input)}")
