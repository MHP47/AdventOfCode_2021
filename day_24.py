from utils import *


class ALU():
    def __init__(self, commands) -> None:
        self.vars = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.commands_list = [tuple(x.split(' ')) for x in commands.splitlines()]

    def run(self, number):
        nums = deque(number)
        for c, *o in self.commands_list:
            if c == 'inp':
                self.inp(*o, nums.popleft())
            else:
                getattr(self, c)(*o)

    def inp(self, a, b):
        self.vars[a] = b

    def add(self, a, b):
        try:
            tmp = int(b)
        except ValueError:
            tmp = self.vars[b]
            
        self.vars[a] += tmp

    def mul(self, a, b):
        try:
            tmp = int(b)
        except ValueError:
            tmp = self.vars[b]

        self.vars[a] *= tmp

    def div(self, a, b):
        try:
            tmp = int(b)
        except ValueError:
            tmp = self.vars[b]

        self.vars[a] //= tmp

    def mod(self, a, b):
        try:
            tmp = int(b)
        except ValueError:
            tmp = self.vars[b]

        self.vars[a] %= tmp

    def eql(self, a, b):
        try:
            tmp = int(b)
        except ValueError:
            tmp = self.vars[b]

        self.vars[a] = 1 if self.vars[a] == tmp else 0

    def display(self):
        print(f'W: {self.vars["w"]} X: {self.vars["x"]} Y: {self.vars["y"]} Z: {self.vars["z"]} ')
        # pprint(list(enumerate(self.commands_list,1)))
        # return f'W: {self.vars["w"]}\nX: {self.vars["x"]}\nY: {self.vars["y"]}\nZ: {self.vars["z"]}\n'

    def get(self):
        if self.vars['z'] == 0:
            return True
        return False
    
    def proc(self, number):
        assert(9999999999999 < number <= 99999999999999)
        nums = deque(map(int, list(str(number))))

        n1 = nums.popleft()
        self.vars['z'] = n1 + 1

        n2 = nums.popleft()
        self.vars['z'] *= 26
        self.vars['z'] += n2 + 7

        n3 = nums.popleft()
        self.vars['z'] *= 26
        self.vars['z'] += n3 + 13

        n4 = nums.popleft()
        x = 0 if (self.vars['z']%26)-6 == n4 else 1
        self.vars['z'] //= 26
        self.vars['z'] = (self.vars['z']*(25+x)+n4+10) if x == 1 else self.vars['z']

        n5 = nums.popleft()
        self.vars['z'] *= 26
        self.vars['z'] += n5

        n6 = nums.popleft()
        x = 0 if (self.vars['z']%26)-4 == n6 else 1
        self.vars['z'] //= 26
        self.vars['z'] = (self.vars['z']*(25+x)+n6+13) if x == 1 else self.vars['z']

        n7 = nums.popleft()
        self.vars['z'] *= 26
        self.vars['z'] += n7 + 11

        n8 = nums.popleft()
        self.vars['z'] *= 26
        self.vars['z'] += n8 + 6

        n9 = nums.popleft()
        self.vars['z'] *= 26
        self.vars['z'] += n9 + 1

        n10 = nums.popleft()
        x = 0 if (self.vars['z']%26)-0 == n10 else 1
        self.vars['z'] //= 26
        self.vars['z'] = (self.vars['z']*(25+x)+n10+7) if x == 1 else self.vars['z']

        n11 = nums.popleft()
        x = 0 if (self.vars['z']%26)-0 == n11 else 1
        self.vars['z'] //= 26
        self.vars['z'] = (self.vars['z']*(25+x)+n11+11) if x == 1 else self.vars['z']

        n12 = nums.popleft()
        x = 0 if (self.vars['z']%26)-3 == n12 else 1
        self.vars['z'] //= 26
        self.vars['z'] = (self.vars['z']*(25+x)+n12+14) if x == 1 else self.vars['z']

        n13 = nums.popleft()
        x = 0 if (self.vars['z']%26)-9 == n13 else 1
        self.vars['z'] //= 26
        self.vars['z'] = (self.vars['z']*(25+x)+n13+4) if x == 1 else self.vars['z']

        n14 = nums.popleft()
        x = 0 if (self.vars['z']%26)-9 == n14 else 1
        self.vars['z'] //= 26
        self.vars['z'] = (self.vars['z']*(25+x)+n14+10) if x == 1 else self.vars['z']


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
    pass


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
