from itertools import product
import numpy as np

def day18(inps, part2=False, steps=100):
    alive = parse_board(inps)
    if part2:
        alive[[0,0,-1,-1], [0,-1,0,-1]] = True
    for step in range(steps):
        alive = step_GOL(alive)
        if part2:
            alive[[0,0,-1,-1], [0,-1,0,-1]] = True
    return alive.sum()

def parse_board(inps):
    indat = np.array(list(map(list, inps.split('\n'))))
    alive = indat == '#'
    return alive

def step_GOL(alive):
    nx,ny = alive.shape
    tboard = np.pad(alive, 1, mode='constant')
    shifteds = np.stack([tboard[1+deltax:1+deltax+nx,1+deltay:1+deltay+ny] for deltax,deltay in product([-1,0,1],repeat=2) if deltax!=0 or deltay!=0], axis=-1)
    neighbsum = shifteds.sum(axis=-1)
    alive = np.where(alive, (neighbsum==2) | (neighbsum==3), neighbsum==3)
    return alive

if __name__ == "__main__":
    inps = open('day18.testinp','r').read().strip()
    print(day18(inps, steps=4))
    print(day18(inps, part2=True, steps=5))
    inps = open('day18.inp','r').read().strip()
    print(day18(inps))
    print(day18(inps, part2=True))
