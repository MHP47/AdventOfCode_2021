import functools
from utils import *


class Grid(dict):
    """A 2D grid, implemented as a mapping of {(x, y): cell_contents}."""
    def __init__(self, mapping=(), rows=()):
        """Initialize with, e.g., either `mapping={(0, 0): 1, (1, 0): 2, ...}`,
        or `rows=[(1, 2, 3), (4, 5, 6)]."""
        self.update(mapping if mapping else
                    {(x, y): val 
                     for y, row in enumerate(rows) 
                     for x, val in enumerate(row)})
        self.width  = max(x for x, y in self) + 1
        self.height = max(y for x, y in self) + 1
    
    def copy(self): return Grid(self)
    
    def next(self, point):
        x, y = point
        x = x+1 if self[point] == '>' else x
        x = 0 if x == self.width else x
        y = y+1 if self[point] == 'v' else y
        y = 0 if y == self.height else y
        return (x,y)

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self[(x,y)], end='')
            print()
        print()



def part_1(p_Input):
    grid = Grid(rows=p_Input.splitlines())
    for i in itertools.count(1):
        dirg = grid.copy()
        for o,n in [(k,dirg.next(k))for k,v in dirg.items() if v == '>' and dirg[dirg.next(k)] == '.']:
            dirg[o] = '.'
            dirg[n] = '>'

        for o,n in [(k,dirg.next(k))for k,v in dirg.items() if v == 'v' and dirg[dirg.next(k)] == '.']:
            dirg[o] = '.'
            dirg[n] = 'v'
        
        if grid == dirg: break
        grid = dirg.copy()
    
    return i
    

example_input_1 = '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
'''
challenge_input = Input('25')

if __name__ == '__main__':
    assert(part_1(example_input_1) == 58)
    print(f"Part 1: {part_1(challenge_input)}")
