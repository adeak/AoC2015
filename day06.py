import numpy as np

def day06(inps, part2=False):
    lights = np.zeros((1000, 1000), dtype=np.int64)
    if part2:
        lims = 0, np.inf
    else:
        lims = 0, 1
    for inp in inps.strip().split('\n'):
        words = inp.split(' ')
        xfrom,yfrom = parseints(words[-3])
        xto,yto = parseints(words[-1])
        if inp.startswith('toggle'):
            if part2:
                lights[xfrom:xto+1,yfrom:yto+1] += 2
            else:
                lights[xfrom:xto+1,yfrom:yto+1] = 1 - lights[xfrom:xto+1,yfrom:yto+1]
        elif inp.startswith('turn on'):
            lights[xfrom:xto+1,yfrom:yto+1] = np.clip(lights[xfrom:xto+1,yfrom:yto+1] + 1, *lims)
        elif inp.startswith('turn off'):
            lights[xfrom:xto+1,yfrom:yto+1] = np.clip(lights[xfrom:xto+1,yfrom:yto+1] - 1, *lims)

    return lights.sum()

def parseints(word):
    return map(int,word.split(','))

if __name__ == "__main__":
    inps = open('day06.inp').read()
    print(day06(inps))
    print(day06(inps, part2=True))
