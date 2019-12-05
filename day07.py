def day07(inps, override=None):
    signals = {}
    inps = inps.strip().split('\n')
    while len(inps) > 0:
        for inp in inps[::-1]:
            gate,op1,op2,target = parse_gate(inp)
            if override is not None and target in override:
                signals[target] = override[target]
                inps.remove(inp)
                continue
            if (not op1.isdigit() and op1 not in signals) or (op2 is not None and not op2.isdigit() and op2 not in signals):
                # we need hitherto-unset signals, get next (previous) input for now
                continue
            if op1.isdigit():
                op1 = int(op1)
            else:
                op1 = signals[op1]
            if op2 is not None and op2.isdigit():
                op2 = int(op2)
            elif op2 is not None:
                op2 = signals[op2]
            if gate == 'SET':
                res = op1
            elif gate == 'NOT':
                res = (~op1) & 65535
            elif gate == 'AND':
                res = op1 & op2
            elif gate == 'OR':
                res = op1 | op2
            elif gate == 'RSHIFT':
                res = op1 >> op2
            elif gate == 'LSHIFT':
                res = op1 << op2
            else:
                assert False, f'Invalid gate found: {gate}!'
            signals[target] = res
            inps.remove(inp)
    return signals['a']
    

def parse_gate(line):
    words = line.split(' ')
    target = words[-1]
    if any(gate in line for gate in ('AND','OR','LSHIFT','RSHIFT')):
        gate = words[1]
        op1,op2 = words[0],words[2]
    elif line.startswith('NOT'):
        gate = 'NOT'
        op1 = words[1]
        op2 = None
    else:
        gate = 'SET'
        op1 = words[0]
        op2 = None
    return gate,op1,op2,target

if __name__ == "__main__":
    inps = open('day07.inp').read()
    a_signal = day07(inps)
    print(a_signal) # part 1
    print(day07(inps, override={'b': a_signal})) # part 2
