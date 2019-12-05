import numpy as np

def day03(inp, part2=False):
    posnow1 = [0,0]
    posnow2 = [0,0]
    allpos = {tuple(posnow1)}
    for i,c in enumerate(inp.strip()):
        if part2 and i%2:
            posnow = posnow1
        else:
            posnow = posnow2
        if c == '^':
            posnow[1] += 1
        elif c == 'v':
            posnow[1] -= 1
        elif c == '>':
            posnow[0] += 1
        elif c == '<':
            posnow[0] -= 1
        allpos.add(tuple(posnow))

    return len(allpos)

if __name__ == "__main__":
    inps = open('day03.inp').read()
    print(day03(inps))
    print(day03(inps, part2=True))
