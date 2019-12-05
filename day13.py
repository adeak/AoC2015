import numpy as np
from itertools import permutations

def day13(inps, part2=False):
    names = {}
    dists = []
    for inp in inps.strip().split('\n'):
        words = inp[:-1].split(' ')
        cfrom,cto,sign,dist = words[0],words[-1],words[2],int(words[3])
        if sign == 'lose':
            dist = -dist
        dists.append((cfrom,cto,dist))
        for c in cfrom,cto:
            if c not in names:
                names[c] = len(names)
    nlen = len(names)
    dmat = np.zeros((nlen,nlen), dtype=np.int64)
    for cfrom,cto,dist in dists:
        i,j = (names[c] for c in (cfrom,cto))
        dmat[i,j] = dist
    if part2:
        nlen += 1
        dm = np.zeros((nlen,nlen), dtype=np.int64)
        dm[:-1,:-1] = dmat
        dmat = dm
    dmat = (dmat + dmat.T)

    dist = -np.inf
    for npath in permutations(range(1, nlen)):
        pfrom,pto = np.append(0, npath), np.append(npath, 0)
        dist = max(dist, dmat[pfrom,list(pto)].sum())
    return dist


if __name__ == "__main__":
    # inps = open('day13.testinp').read()
    inps = open('day13.inp').read()
    print(day13(inps))
    print(day13(inps, part2=True))
