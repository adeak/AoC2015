def day10(inp, numsteps=40):
    out = inp
    for _ in range(numsteps):
        out = looksay(out)
    return len(out)

def looksay(inp):
    char = inp[0]
    count = 1
    out = []
    for k in inp[1:]:
        if k == char:
            count += 1
        else:
            out.append(str(count) + char)
            char = k
            count = 1
    return ''.join(out + [str(count) + char])

if __name__ == "__main__":
    inp = open('day10.inp').read().strip()
    print(day10(inp))  # part 1
    print(day10(inp, 50))  # part 2
