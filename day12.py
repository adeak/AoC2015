import re
from ast import literal_eval

def day12(inp):
    # part 1: sum all numbers
    part1 = sum(map(int,re.sub(r'[^\d-]+',' ',inp).strip().split()))
    # part 2: proper parsing; have to ignore dicts with keys with "red"
    part2 = recursive_parser(literal_eval(inp))
    return part1, part2

def recursive_parser(objs):
    if isinstance(objs, str):
        return 0
    if isinstance(objs, int):
        return objs
    if isinstance(objs, list):
        return sum(recursive_parser(obj) for obj in objs)
    if isinstance(objs, dict):
        if 'red' in objs.values():
            return 0
        return sum(recursive_parser(obj) for obj in objs.values())


if __name__ == "__main__":
    inp = open('day12.inp').read()
    print(day12(inp))
