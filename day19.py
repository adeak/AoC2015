import re

def day19(inps):
    allinps = inps.strip().split('\n')
    initmol = allinps[-1]
    results = set()
    rules = []
    for inp in allinps[:-2]:
        cfrom,cto = inp.strip().split(' => ')
        rules.append([cfrom, cto])
    for cfrom,cto in rules:
        for matches in re.finditer(cfrom, initmol):
            span = matches.span()
            mol = initmol[:span[0]] + cto + initmol[span[1]:]
            results.add(mol)
    return len(results)

def day19b_rev(inps):
    # reversed rules
    # v2: sort rules in descending order of target length, do DFS
    allinps = inps.strip().split('\n')
    target = 'e'
    initmol = allinps[-1]
    rules = []
    intermeds = {initmol}
    for inp in allinps[:-2]:
        cfrom,cto = inp.strip().split(' => ')
        # reverse the rules and the search direction
        # v2: sort rules in descending order of 
        rules.append([cto,cfrom])
    rules = sorted(rules, key=lambda x:len(x[0]), reverse=True) # remember: now cto is the original product molecule!
    molpath = [initmol]
    repsteps = []
    # molpath: list containing the path of molecules taken, for backtracking
    # repsteps contains 2-tuples: rule/pos for the rule taken, and pos for the case where there were multiple matches
    # when we backtrack, we iterate over next valid pos'es, then over next rules, then go back a molecule if we're out of options
    while True: # loop over molecules
        molnow = molpath[-1]
        nextstep = False
        irulenow,imatchnow = (0,0) # start from rule 1 with each new molecule
        while True: # loop over replacements
            for irule,(cfrom,cto) in enumerate(rules[irulenow:], start=irulenow):
                if cfrom in molnow:
                    # do a replacement
                    for imatch,match in enumerate(re.finditer(cfrom, molnow)):
                        if irule == irulenow and imatch < imatchnow:
                            continue
                        span = match.span()
                        mol = molnow[:span[0]] + cto + molnow[span[1]:]
                        if mol == target:
                            # we're done, get number of steps
                            return len(molpath)
                        molpath.append(mol)
                        repsteps.append((irule, imatch))
                        nextstep = True
                        break
                    else:
                        # we ran out of backtracking/pattern matching
                        # we need to go back a molecule and start from scratch
                        molpath.pop()
                        nextstep = True
                if nextstep:
                    break
            if nextstep:
                # we found a new level, carry on in outer loop with next molecule
                break
            else:
                # we need to backtrack to the previous replacement's level
                # with the previous molecule
                molnow = molpath.pop()
                irulenow,imatchnow = repsteps.pop()
                imatchnow += 1 # start from next occurence, or next rule if this was the last one
            
def iterate_mol(rules, initmol):
    results = set()
    for cfrom,cto in rules:
        for matches in re.finditer(cfrom,initmol):
            span = matches.span()
            mol = initmol[:span[0]] + cto + initmol[span[1]:]
            results.add(mol)
    return results

if __name__ == "__main__":
    inps = open('day19.testinp').read().strip()
    print(day19(inps))
    inps = open('day19.testinp2').read().strip()
    print(day19b_rev(inps))
    inps = open('day19.inp','r').read().strip()
    print(day19(inps))
    print(day19b_rev(inps))
