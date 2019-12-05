from hashlib import md5

def day04(inp, part2=False):
    if isinstance(inp, str):
        inp = inp.encode('ascii')
    if part2:
        numzeros = 6
    else:
        numzeros = 5
    ind = 0
    while True:
        hexhash = md5(inp + str(ind).encode('ascii')).hexdigest()
        if hexhash.startswith('0' * numzeros):
            return ind
        ind += 1

if __name__ == "__main__":
    inp = open('day04.inp').read().strip()
    print(day04(inp))
    print(day04(inp, part2=True))
