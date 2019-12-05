from collections import Counter

def day05(inps, part2=False):
    if part2:
        is_nice_fun = is_nice_v2
    else:
        is_nice_fun = is_nice
    return sum(map(is_nice_fun, inps.strip().split('\n')))

def is_nice(word):
    counter = Counter(word)
    if sum(counter[c] for c in 'aeiou') < 3:
        return False

    if any(k in word for k in ('ab','cd','pq','xy')):
        return False

    for i,k in enumerate(word[:-1]):
        if word[i] == word[i+1]:
            return True

    return False

def is_nice_v2(word):
    for i,k in enumerate(word[:-2]):
        if word[i] == word[i+2]:
            break
    else:
        return False

    for i,k in enumerate(word[:-1]):
        if word[i:i+2] in word[:i] or word[i:i+2] in word[i+2:]:
            break
    else:
        return False

    return True


if __name__ == "__main__":
    inps = open('day05.inp').read()
    print(day05(inps))
    print(day05(inps, part2=True))
