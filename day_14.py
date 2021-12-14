from utils import *


def part_1(p_Input):
    template, rules = p_Input.split('\n\n')
    rules = {k:v for k,v in [x.split(' -> ') for x in rules.splitlines()]}
    for s in range(1,11):
        new_str = ''
        for x in [template[i:i+2] for i in range(0, len(template)-1)]:
            new_str += x[0] + rules[x]
        new_str += template[-1]
        template = new_str
    mc = Counter(template).most_common()
    return mc[0][1] - mc[-1][1]

def part_2(p_Input, p_Steps=40):
    template, rules = p_Input.split('\n\n')
    rules = {k:v for k,v in [x.split(' -> ') for x in rules.splitlines()]}
    elements = Counter(template)
    pairings = Counter([cat(x) for x in zip(template,template[1:])])
    for _ in range(p_Steps):
        tmp_pairings = pairings.copy()
        for (x,y),z in rules.items():
            c = tmp_pairings[x+y]
            pairings[x+y] -= c
            pairings[x+z] += c
            pairings[z+y] += c
            elements[z] += c
    mc = elements.most_common()
    return mc[0][1] - mc[-1][1]
    

example_input_1 = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''
challenge_input = Input('14')

assert(part_1(example_input_1) == 1588)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1, 10) == 1588)
assert(part_2(example_input_1, 40) == 2188189693529)
print(f"Part 2: {part_2(challenge_input)}")
