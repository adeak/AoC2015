from itertools import chain,combinations
from math import ceil

def day21(inps, part2=False, HP=100):
    boss = {}
    for inp in inps.strip().split('\n'):
        val = int(inp.split()[-1])
        if inp.startswith('Hit Points'):
            key = 'HP'
        elif inp.startswith('Damage'):
            key = 'attack'
        elif inp.startswith('Armor'):
            key = 'defense'
        else:
            print('invalid input: {}'.format(inp))
            return
        boss[key] = val

    weapons = [(8, 4, 0),
               (10, 5, 0),
               (25, 6, 0),
               (40, 7, 0),
               (74, 8, 0)]
    armors = [(0,0,0),
              (13, 0, 1),
              (31, 0, 2),
              (53, 0, 3),
              (75, 0, 4),
              (102, 0, 5)]
    rings = [(25, 1, 0),
             (50, 2, 0),
             (100, 3, 0),
             (20, 0, 1),
             (40, 0, 2),
             (80, 0, 3)]

    # choose a weapon, n armor (including no armor), and up to 2 rings
    if part2:
        compfun = max
    else:
        compfun = min
    bestcost = -compfun(-float('inf'),float('inf')) # min -> +inf, max -> -inf
    for w_cost,w_att,w_def in weapons:
        for a_cost,a_att,a_def in armors:
            for trings in chain(combinations(rings,0), combinations(rings,1), combinations(rings,2)):
                if len(trings) == 0:
                    r_cost,r_att,r_def = 0,0,0
                elif len(trings) == 1:
                    r_cost,r_att,r_def = trings[0]
                else:
                    r_cost,r_att,r_def = (trings[0][k]+trings[1][k] for k in range(3))

                win_eh = will_win(boss, HP, w_att + a_att + r_att, w_def + a_def + r_def)
                # accept if (part1 and win) or (part2 and lose): XOR(part2,win)
                if part2 ^ win_eh:
                    cost = w_cost + a_cost + r_cost
                    bestcost = compfun(bestcost, cost)
    return bestcost

def will_win(boss,HP,attack,defense):
    # number of turns we need in order to kill boss
    n_PC = ceil(boss['HP']/max(attack-boss['defense'],1))
    # number of turns we need in order to bite the dust
    n_boss = ceil(HP/max(boss['attack']-defense,1))
    # we win if n_PC<=n_boss (we hit first)
    return n_PC <= n_boss

if __name__ == "__main__":
    inps = open('day21.inp').read()
    print(day21(inps))
    print(day21(inps, part2=True))
