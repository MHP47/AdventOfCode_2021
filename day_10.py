from utils import *

OPENS = '({[<'
CLOSES = ')}]>'
SCORES = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
SCORES_2 = { ')': 1, ']': 2, '}': 3, '>': 4 }

def part_1(p_Input):
    score = 0
    data = p_Input.splitlines()
    for i, r in enumerate(data, 1):
        p = ''
        while p != r:
            p = r
            r = re.sub(r'\[\]|{}|\(\)|<>', '', r)
        if not all([x in OPENS for x in r]):
            illegal_char = re.search(r'[\[{\(<][\]}\)>]', r).group()[-1]
            score += SCORES[illegal_char]
    return score

def part_2(p_Input):
    data = p_Input.splitlines()
    scores = []
    for i, r in enumerate(data):
        p = ''
        while p != r:
            p = r
            r = re.sub(r'\[\]|{}|\(\)|<>', '', r)
        if all([x in OPENS for x in r]):
            score = 0
            for x in r[::-1]:
                score *= 5
                score += SCORES_2[CLOSES[OPENS.index(x)]]
            scores.append(score)
    return sorted(scores)[(len(scores)-1)//2]



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

assert(part_2(example_input_1) == 288957)
print(f"Part 2: {part_2(challenge_input)}")
