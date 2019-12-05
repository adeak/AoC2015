import numpy as np
from itertools import permutations

def day09(inps):
    names = {}
    dists = []
    for inp in inps.strip().split('\n'):
        words = inp.split(' ')
        cfrom,cto,dist = words[0],words[2],int(words[-1])
        dists.append((cfrom,cto,dist))
        for c in cfrom,cto:
            if c not in names:
                names[c] = len(names)

    nlen = len(names)
    dmat = np.zeros((nlen,nlen), dtype=np.int64)
    for cfrom,cto,dist in dists:
        i,j = (names[c] for c in (cfrom,cto))
        dmat[i,j] = dmat[j,i] = dist

    dmat0 = dmat
    results = []
    for compfun in min,max:
        dmat = np.array(dmat0)
        dist = -compfun(-np.inf,np.inf) # min -> +inf, max -> -inf
        for npath in permutations(range(nlen)):
            pfrom,pto = npath[:-1],npath[1:]
            dist = compfun(dist, dmat[pfrom, list(pto)].sum())
        results.append(dist)

    return tuple(results)


if __name__ == "__main__":
    inps = open('day09.inp').read()
    print(day09(inps))
