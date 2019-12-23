from itertools import combinations

def day17(inps, part2=False, V=150):
    containers = sorted(list(map(int,inps.strip().split('\n'))))[::-1]

    combins = 0
    for n in range(1, len(containers) + 1):
        for partconts in combinations(containers, n):
            if sum(partconts) == V:
                combins += 1
        if part2 and combins > 0:
            break

    return combins

if __name__ == "__main__":
    inps = open('day17.testinp','r').read()
    print(day17(inps, V=25))
    print(day17(inps,part2=True, V=25))
    inps = open('day17.inp','r').read()
    print(day17(inps))
    print(day17(inps, part2=True))
