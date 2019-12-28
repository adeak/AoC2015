def day23(inps, astart=0):
    regs = {k: 0 for k in list('ab')}
    regs['a'] = astart
    instrs = inps.strip().split('\n')
    i = 0
    while True:
        if i<0 or i==len(instrs):
            return regs['b']

        inst = instrs[i]
        tlist = inst.split(' ')
        if tlist[0] == 'inc':
            reg = tlist[1]
            regs[reg] += 1
        elif tlist[0] == 'hlf':
            reg = tlist[1]
            regs[reg] /= 2
        elif tlist[0] == 'tpl':
            reg = tlist[1]
            regs[reg] *= 3
        elif tlist[0] == 'jmp':
            delta = int(tlist[1])
            i += delta
            continue
        elif tlist[0].startswith('ji'):
            cond = tlist[1][0]
            delta = int(tlist[2])
            if cond in regs:
                cond = regs[cond]
            else:
                cond = int(cond)

            if (tlist[0] == 'jie' and cond % 2 == 0) or (tlist[0] == 'jio' and cond == 1):
                i += delta
                continue
        else:
            raise ValueError(f'weird input: {inst}')

        i += 1

if __name__ == "__main__":
    inps = open('day23.inp').read()
    print(day23(inps))
    print(day23(inps, astart=1))
