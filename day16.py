import operator

def day16(inps, part2=False):
    pattern = {'children': 3,
               'cats': 7,
               'samoyeds': 2,
               'pomeranians': 3,
               'akitas': 0,
               'vizslas': 0,
               'goldfish': 5,
               'trees': 3,
               'cars': 2,
               'perfumes': 1}

    if part2:
        checkfun1 = operator.ge
        checkfun2 = operator.le
        checkfun3 = operator.ne
    else:
        checkfun1 = checkfun2 = checkfun3 = operator.ne

    for i,inp in enumerate(inps.strip().split('\n'),1):
        *_,dat = inp.partition(': ')
        for props in dat.split(', '):
            key,_,val = props.partition(': ')
            if key in ('cats','trees'):
                if checkfun1(pattern[key],int(val)):
                    break
            elif key in ('pomeranians','goldfish'):
                if checkfun2(pattern[key],int(val)):
                    break
            else:
                if checkfun3(pattern[key],int(val)):
                    break
        else:
            return i


if __name__ == "__main__":
    inps = open('day16.inp').read()
    print(day16(inps))
    print(day16(inps, part2=True))
