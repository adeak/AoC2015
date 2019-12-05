from io import StringIO
import numpy as np

def day02(inp):
    dat = np.loadtxt(StringIO(inp), delimiter='x', dtype=int)
    dat.sort(axis=1)
    part1 = (dat[:,:-1].prod(axis=1) + 2*(dat[:,0]*dat[:,1]+dat[:,0]*dat[:,2]+dat[:,1]*dat[:,2])).sum()
    part2 = (dat.prod(axis=1) + 2*(dat[:,:-1].sum(axis=1))).sum()
    return part1, part2

if __name__ == "__main__":
    inp = open('day02.inp').read()
    print(day02(inp))
