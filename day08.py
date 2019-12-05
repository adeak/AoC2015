from ast import literal_eval
from re import escape

def day08(inps):
    codelen = 0
    strlen = 0
    encodelen = 0
    for inp in inps.strip().split('\n'):
        codelen += len(inp)
        strlen += len(literal_eval(inp))
        encodelen += len(escape(inp).replace('"', r'\"')) + 2 # don't forget "" around...
    part1 = codelen - strlen
    part2 = encodelen - codelen
    return part1, part2


if __name__ == "__main__":
    testinps = open('day08.testinp').read()
    print(day08(testinps))
    inps = open('day08.inp').read()
    print(day08(inps))
