from collections import defaultdict
from functools import reduce
import operator

def prod(it):
    """product of iterable as per http://stackoverflow.com/a/595409/5067311"""
    return reduce(operator.mul, it, 1)

def day15(inps,part2=False):
    ingreds = defaultdict(dict)
    props = set()
    for inp in inps.strip().split('\n'):
        name,rest = inp.split(':')
        for r in rest.strip().split(','):
            rr = r.strip().split()
            prop = rr[0]
            score = int(rr[1])
            ingreds[name][prop] = score
            props.add(prop)

    maxscore = 0
    for ratios in partition(100,len(ingreds)):
        if part2 and sum(r*ingreds[name]['calories'] for r,name in zip(ratios,ingreds)) != 500:
            continue
        scorenow = prod(max(0,sum(r*ingreds[name][prop] for r,name in zip(ratios,ingreds))) for prop in props if prop != 'calories')
        if scorenow > maxscore:
            maxscore = scorenow
    return maxscore


def partition(N, nparts):
    """Generate partitions of N to nparts using recursion"""
    if nparts == 1:
        yield [N]
        return

    for k in range(N+1):
        for parts in partition(N-k, nparts-1):
            yield [k] + parts


if __name__ == "__main__":
    inps = open('day15.testinp').read()
    print(day15(inps))
    print(day15(inps, part2=True))
    inps = open('day15.inp').read()
    print(day15(inps))
    print(day15(inps, part2=True))
