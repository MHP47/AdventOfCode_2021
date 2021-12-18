from utils import *
import ast


def snail_add(a,b):
    n = [a]
    n.append(b)
    return snail_reduce(n)


def snail_reduce(p_Number):
    while snail_explode(p_Number) or snail_split(p_Number):
        pass
    return p_Number


def snail_explode(p_Number, depth=[]):
    # This function (ab)uses (IMO) Python's pass-by-reference-value tactic
    # Allows it to manipulate the object, while returning True/False only
    if type(p_Number) == int:
        return False
    if len(depth) < 4:
        # Recursion bullshit
        # Look at the left and right pair separately through own recursion stacks
        # Transform each half to a tuple, with 0 to signify left, and 1 for right
        return snail_explode(p_Number[0], depth+[(p_Number, 0)]) or snail_explode(p_Number[1], depth+[(p_Number, 1)])
    # Find the left number (if exists)
    for (snumber, side) in reversed(depth):
        if side == 1:# i.e. snumber is the right of
            if type(snumber[0]) == int:
                snumber[0] += p_Number[0]
            else:
                snumber = snumber[0]
                while type(snumber[1]) != int:
                    snumber = snumber[1]
                snumber[1] += p_Number[0]
            break
    # Find the right number (if exists)
    for (snumber, side) in reversed(depth):
        if side == 0: # i.e. snumber is the left of
            if type(snumber[1]) == int:
                # Value is an int, so increment it by the exploded number
                # i.e. p_Number is the value to explode, and snumber is the value to increment (because recursion)
                snumber[1] += p_Number[1]
            else:
                # Loop until find an int(pair) to action
                snumber = snumber[1]
                while type(snumber[0]) != int:
                    snumber = snumber[0]
                snumber[0] += p_Number[1]
            break
    # The last depth is the exploded value, which gets set to 0
    x,y = depth[-1]
    x[y] = 0
    return True


def snail_explode_test(p_Number):
    # Function not used, only for testing
    snail_explode(p_Number)
    return p_Number


def snail_split(p_Number, depth=[]):
    # Using the same bullshit tactics from exploding
    if type(p_Number) == int:
        if p_Number < 10:
            return False
        x,y = depth[-1]
        x[y] = [p_Number//2, math.ceil(p_Number/2)]
        return True
    return snail_split(p_Number[0], depth+[(p_Number, 0)]) or snail_split(p_Number[1], depth+[(p_Number, 1)])


def snail_split_test(p_Number):
    # Function not used, only for testing
    snail_split(p_Number)
    return p_Number


def snail_magnitude(p_Number):
    if type(p_Number) == int:
        return p_Number
    return 3*snail_magnitude(p_Number[0]) + 2*snail_magnitude(p_Number[1])


def part_1(p_Input):
    snail_numbers = [ast.literal_eval(i) for i in p_Input.splitlines()]
    total = snail_numbers[0]
    for n in snail_numbers[1:]:
        total = snail_add(total, n)
    return snail_magnitude(total)

def part_2(p_Input):
    snail_numbers = itertools.permutations(p_Input.splitlines(), 2)
    max_magnitude = 0

    for a,b in snail_numbers:
        max_magnitude = max(max_magnitude, snail_magnitude(snail_add(ast.literal_eval(a), ast.literal_eval(b))))
    
    return max_magnitude


example_input_1 = '''[1,1]
[2,2]
[3,3]
[4,4]
'''
example_input_2 = '''[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
'''
example_input_3 = '''[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
'''
example_input_4 = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
'''
example_input_5 = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
'''
challenge_input = Input('18')

# Magnitude checks
assert(snail_magnitude([[1,2],[[3,4],5]]) == 143)
assert(snail_magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384)
assert(snail_magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445)
assert(snail_magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791)
assert(snail_magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137)
assert(snail_magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488)
assert(snail_magnitude([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]) == 4140)
# Exploding checks
assert(snail_explode_test([[[[[9,8],1],2],3],4]) == [[[[0,9],2],3],4])
assert(snail_explode_test([7,[6,[5,[4,[3,2]]]]]) == [7,[6,[5,[7,0]]]])
assert(snail_explode_test([[6,[5,[4,[3,2]]]],1]) == [[6,[5,[7,0]]],3])
assert(snail_explode_test([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
assert(snail_explode_test([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[7,0]]]])
# Split checks
assert(snail_split_test([[[[0,7],4],[15,[0,13]]],[1,1]]) == [[[[0,7],4],[[7,8],[0,13]]],[1,1]])
assert(snail_split_test([[[[0,7],4],[[7,8],[0,13]]],[1,1]]) == [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])

assert(part_1(example_input_4) == 3488)
assert(part_1(example_input_5) == 4140)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_5) == 3993)
print(f"Part 2: {part_2(challenge_input)}")
