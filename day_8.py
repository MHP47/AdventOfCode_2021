from utils import *


NUMBER_DIGITS = {
'012456': '0',
'25': '1',
'02346': '2',
'02356': '3',
'1235': '4',
'01356': '5',
'013456': '6',
'025': '7',
'0123456': '8',
'012356': '9'
}


def part_1(p_Input):
    count = 0
    for i in p_Input.splitlines():
        signal_patterns, output_val = i.split(' | ')
        signal_patterns = signal_patterns.split(' ')
        output_val = output_val.split(' ')
        count += len([x for x in output_val if len(x) in (2,4,3,7)])
    return count


def part_2(p_Input):
    TOTAL = 0
    data = [(y.split(' '), z.split(' ')) for y,z in [x.split(' | ') for x in p_Input.splitlines()]]
    for signal_patterns, output_val in data:
        numbers = defaultdict(lambda: set(alphabet))
        # Proc knowns first
        for pattern in [x for x in signal_patterns if len(x) in (2,4,3,7)]:
            if len(pattern) == 2:
                # 1
                numbers[2] = numbers[2].intersection(set(pattern))
                numbers[5] = numbers[5].intersection(set(pattern))
            elif len(pattern) == 4:
                # 4
                numbers[1] = numbers[1].intersection(set(pattern))
                numbers[2] = numbers[2].intersection(set(pattern))
                numbers[3] = numbers[3].intersection(set(pattern))
                numbers[5] = numbers[5].intersection(set(pattern))
            elif len(pattern) == 3:
                # 7
                numbers[0] = numbers[0].intersection(set(pattern))
                numbers[2] = numbers[2].intersection(set(pattern))
                numbers[5] = numbers[5].intersection(set(pattern))
            elif len(pattern) == 7:
                # 8
                numbers[0] = numbers[0].intersection(set(pattern))
                numbers[1] = numbers[1].intersection(set(pattern))
                numbers[2] = numbers[2].intersection(set(pattern))
                numbers[3] = numbers[3].intersection(set(pattern))
                numbers[4] = numbers[4].intersection(set(pattern))
                numbers[5] = numbers[5].intersection(set(pattern))
                numbers[6] = numbers[6].intersection(set(pattern))

        fives = Counter(flatten([x for x in signal_patterns if len(x) == 5]))
        sixes = Counter(flatten([x for x in signal_patterns if len(x) == 6]))

        numbers[0] = numbers[0].intersection(set([k for k,v in fives.items() if v == 3]))
        numbers[3] = numbers[3].intersection(set([k for k,v in fives.items() if v == 3]))
        numbers[6] = numbers[6].intersection(set([k for k,v in fives.items() if v == 3]))
        numbers[2] = numbers[2].intersection(set([k for k,v in fives.items() if v == 2]))
        numbers[5] = numbers[5].intersection(set([k for k,v in fives.items() if v == 2]))
        numbers[1] = numbers[1].intersection(set([k for k,v in fives.items() if v == 1]))
        numbers[4] = numbers[4].intersection(set([k for k,v in fives.items() if v == 1]))

        numbers[0] = numbers[0].intersection(set([k for k,v in sixes.items() if v == 3]))
        numbers[1] = numbers[1].intersection(set([k for k,v in sixes.items() if v == 3]))
        numbers[5] = numbers[5].intersection(set([k for k,v in sixes.items() if v == 3]))
        numbers[6] = numbers[6].intersection(set([k for k,v in sixes.items() if v == 3]))
        numbers[2] = numbers[2].intersection(set([k for k,v in sixes.items() if v == 2]))
        numbers[3] = numbers[3].intersection(set([k for k,v in sixes.items() if v == 2]))
        numbers[4] = numbers[4].intersection(set([k for k,v in sixes.items() if v == 2]))

        seen = set()
        digits = dict()
        for k,v in sorted(numbers.items(), key=lambda x: len(x)):
            if len(v - seen) == 1:
                digits[(v - seen).pop()] = str(k)
                seen = seen.union(v)

        TOTAL += int(cat([NUMBER_DIGITS[cat(sorted([digits[x] for x in list(ov)]))] for ov in output_val]))
    return TOTAL

example_input_1 = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''
example_input_2 = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
challenge_input = Input('8')

assert(part_1(example_input_1) == 26)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 61229)
assert(part_2(example_input_2) == 5353)
print(f"Part 2: {part_2(challenge_input)}")
