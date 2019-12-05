import re

def day11(inp):
    passwd_gen = emit_passwd(inp)
    results = []
    for pwd in passwd_gen:
        # generator takes care of forbidden i,o,l

        # check for abc, def, xyz etc
        for k in range(len(pwd)-2):
            if ord(pwd[k])+1 == ord(pwd[k+1]) == ord(pwd[k+2])-1:
                break
        else:
            continue

        # check for two pairs of chars
        if re.search(r'(.)\1.*(.)\2',pwd) is None:
            continue

        results.append(pwd)
        if len(results) == 2:
            return tuple(results)

def emit_passwd(init):
    forbidden = [ord(k) for k in 'iol']
    maxval = ord('z') - ord('a')
    codelen = len(init)
    code = [ord(k)-ord('a') for k in init]
    while True:
        code[-1] += 1
        if code[-1] in forbidden:
            continue
        ic = codelen - 1
        while code[ic]>maxval:
            code[ic] = 0
            ic -= 1
            code[ic] += 1
            while code[ic] in forbidden:
                code[ic] += 1
                code[ic+1:] = [0]*(codelen-ic-1)
        yield ''.join((chr(k+ord('a')) for k in code))


if __name__ == "__main__":
    inp = open('day11.inp').read().strip()
    print(day11(inp))
