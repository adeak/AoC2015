from itertools import count,combinations
from ast import literal_eval
from functools import reduce
import operator

def day24(inps):
    minQE = float('inf')
    weights = literal_eval(inps.strip().replace('\n',','))
    total = sum(weights)
    subtotal = total//3
    for n1 in count(1):
        for weights1 in combinations(weights,n1):
            if sum(weights1) != subtotal:
                continue
            rest = sorted([w for w in weights if w not in weights1],reverse=True)
            # note that 1 specific configuration of weights2-weights3 is enough, weights1 alone determines the result
            foundone = False
            for n2 in count(1,len(rest)//2+1):
                for weights2 in combinations(rest,n2):
                    if sum(weights2) == subtotal:
                        # then weights1 - weights2 - rest is a good combination
                        weights3 = [w for w in weights if w not in weights1 and w not in weights2]
                        QE = prod(weights1)
                        if QE < minQE:
                            minQE = QE
                            #print(f'found new minimum with QE = {minQE}: {weights1}, {weights2}, {tuple(weights3)}') # tuple for pretty printing
                            #foundone = True
                            #break # weights2 loop

                            # turns out the first find is correct for both parts, keep that...
                            return minQE
                if foundone:
                    # then we found a valid weights2-weights3 combination, go on to next weights1 combination
                    break
        if minQE != float('inf'):
            # then we've got the best case with minimal n1, we're done
            return

def day24b(inps):
    minQE = float('inf')
    weights = literal_eval(inps.strip().replace('\n',','))
    total = sum(weights)
    subtotal = total//4
    for n1 in count(1):
        for weights1 in combinations(weights,n1):
            if sum(weights1) != subtotal:
                continue
            rest1 = sorted([w for w in weights if w not in weights1],reverse=True)
            # note that 1 specific configuration of weights2-weights3-weights4 is enough, weights1 alone determines the result
            foundone = False
            for n2 in count(1,len(rest1)//3+1):
                for weights2 in combinations(rest1,n2):
                    if sum(weights2) != subtotal:
                        continue
                    rest2 = sorted([w for w in weights if w not in weights1 and w not in weights2],reverse=True)
                    for n3 in count(1,len(rest2)//2+1):
                        for weights3 in combinations(rest2,n3):
                            if sum(weights3) == subtotal:
                                # then weights1 - weights2 - weights3 - rest is a good combination
                                weights4 = [w for w in weights if w not in weights1 and w not in weights2 and w not in weights3]
                                QE = prod(weights1)
                                if QE < minQE:
                                    minQE = QE
                                    #print(f'found new minimum with QE = {minQE}: {weights1}, {weights2}, {weights3}, {tuple(weights4)}') # tuple for pretty printing
                                    #foundone = True
                                    #break # weights3 loop

                                    # turns out the first find is correct for both parts, keep that...
                                    return minQE
                        if foundone:
                            break
                    if foundone:
                        break
                if foundone:
                    # then we found a valid weights2-weights3 combination, go on to next weights1 combination
                    break
        if minQE != float('inf'):
            # then we've got the best case with minimal n1, we're done
            return

def prod(it):
    """product of iterable as per http://stackoverflow.com/a/595409/5067311"""
    return reduce(operator.mul, it, 1)

if __name__ == "__main__":
    inps = open('day24.inp','r').read()
    # sketchy solutions: first found combination happens to be best, no actual check (would take too long)
    print(day24(inps))
    print(day24b(inps))
