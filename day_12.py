from utils import *


def part_1(p_Input):
    caves = set(flatten([x.split('-') for x in p_Input.splitlines()]))
    mappings = defaultdict(list)
    for s,e in [x.split('-') for x in p_Input.splitlines()]:
        mappings[s].append(e)
        mappings[e].append(s)
    paths = []
    to_proc = deque([['start']])
    while to_proc:
        path = to_proc.popleft()
        for d in mappings[path[-1]]:
            if d == 'end':
                paths.append(path+[d])
            elif d == 'start':
                pass
            elif d == d.lower() and d not in path:
                to_proc.append(path+[d])
            elif d == d.upper():
                to_proc.append(path+[d])
    return len(paths)


def part_2(p_Input):
    pass


example_input_1 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''
example_input_2 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''
example_input_3 = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''
challenge_input = Input('12')

assert(part_1(example_input_1) == 10)
assert(part_1(example_input_2) == 19)
assert(part_1(example_input_3) == 226)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 'None')
print(f"Part 2: {part_2(challenge_input)}")
