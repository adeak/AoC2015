import numpy as np

def day14(inps, dt=2503):
    deerdata = []
    for inp in inps.strip().split('\n'):
        words = inp.split()
        name,speed,t,cooldown = words[0],words[3],words[6],words[-2]
        deerdata.append([speed,t,cooldown])
    deerdata = np.array(deerdata,dtype=np.int64)

    part1 = find_deerpos(deerdata,dt).max()

    # part 2:
    points = np.zeros(deerdata.shape[0],dtype=np.int64)
    for t in range(1,dt+1):
        pos = find_deerpos(deerdata,t)
        maxdist = pos.max()
        points[pos==maxdist] += 1
    part2 = points.max()

    return part1, part2


def find_deerpos(deerdata, dt):
    # find integer blocks of start+stop
    tblock = deerdata[:,1:].sum(axis=1)
    nblocks = dt//tblock

    #the remainder contains up to "t" seconds of moving
    deltat = np.minimum(deerdata[:,1],np.mod(dt,tblock))

    # max distance:
    return (nblocks*deerdata[:,1]+deltat)*deerdata[:,0]


if __name__ == "__main__":
    inps = open('day14.testinp').read()
    print(day14(inps, dt=1000))
    inps = open('day14.inp').read()
    print(day14(inps))
