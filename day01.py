from collections import Counter

def day01(inp):
    c = Counter(inp)
    part1 = c['('] - c[')']
    pos = 0
    for i,k in enumerate(inp):
        if k == '(':
            pos += 1
        else:
            pos -= 1
        if pos < 0:
            part2 = i + 1
            break

    return part1, part2

if __name__ == "__main__":
    inp = open('day01.inp').read()
    print(day01(inp))
