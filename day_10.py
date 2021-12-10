from utils import *

OPENS = '({[<'
CLOSES = ')}]>'
SCORES = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

def part_1(p_Input):
    score = 0
    data = p_Input.splitlines()
    for i, r in enumerate(data, 1):
        p = ''
        while p != r:
            p = r
            for c in (r'\[\]', r'\(\)', '<>', r'{}'):
                r = re.sub(c, '', r)
        if not all([x in OPENS for x in r]):
            illegal_char = re.search(r'[\[{\(<][\]}\)>]', r).group()[-1]
            score += SCORES[illegal_char]
    return score

def part_2(p_Input):
    pass


example_input_1 = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''
challenge_input = Input('10')

assert(part_1(example_input_1) == 26397)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 'None')
print(f"Part 2: {part_2(challenge_input)}")
