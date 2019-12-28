import numpy as np

def day20(inp, part1=True, cap_len=50):
    # use a sieve that's 1/10 the target, should be generous
    gifts = np.zeros(inp//10, dtype=int)
    # index 0 is ignored

    if part1:
        weight = 10
        cap = False
    else:
        weight = 11
        cap = True

    for elf in range(1, gifts.size):
        if cap:
            inds = np.arange(elf, gifts.size, elf)[:cap_len]
            gifts[inds] += weight*elf
        else:
            gifts[elf::elf] += weight*elf

        # check if we're done
        if gifts[elf] > inp:
            return elf

if __name__ == "__main__":
    inp = int(open('day20.inp').read().strip())
    print(day20(inp))
    print(day20(inp, part1=False))
