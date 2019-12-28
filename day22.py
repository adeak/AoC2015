from itertools import count,chain,combinations
from math import ceil

def day22(inps, part2=False, HP=50, mana=500):
    for inp in inps.strip().split('\n'):
        val = int(inp.split()[-1])
        if inp.startswith('Hit Points'):
            boss_HP = val
        elif inp.startswith('Damage'):
            boss_att = val
        else:
            print('invalid input: {}'.format(inp))
            return

    # magic missile - drain - shield - poison - recharge
    costs = [53, 73, 113, 173, 229]
    # MM: instant 4 damage
    # drain: damage +2, heal 2
    # shield: +7 armor for 6 turns
    # poison: +3 damage for 6 turns
    # recharge: +101 mana for 5 turns
    # (timers is a 3-element list for shield-poison-recharge)
    
    bestcost = float('inf')

    # do BFS turn by turn, keep track of mana costs -> abandon paths that are too costly or dead
    # (guaranteed to end in finite time)
    # a given path during BFS: dict with keys: costnow, HPs, mana, timers
    oldpaths = [{'costnow': 0, 'HPs': (HP, boss_HP), 'mana': mana, 'timers': [0, 0, 0]}]
    for k in count():
        # only consider player's turns: boss' turn is deterministic
        newpaths = [] # gather next possible paths here

        if len(oldpaths) == 0:
            return bestcost

        for path in oldpaths:
            costnow = path['costnow']
            timers = path['timers']
            HP,boss_HP = path['HPs']
            mana = path['mana']

            # first take a hit in case of part 2
            if part2:
                HP -= 1
                if HP <= 0:
                    # we're dead, abandon path
                    continue

            # now see if there are active effects, those come first
            timers,boss_HP,mana,defense = step_effects(timers, boss_HP, mana)
            if boss_HP <= 0:
                if costnow < bestcost:
                    bestcost = costnow
                # no further paths from here
                continue

            # now choose a new spell -> spawn new paths
            if mana < min(costs):
                # we're dead
                continue

            for i,cost in enumerate(costs):
                if cost > mana:
                    # insufficient funds
                    continue
                nextmana = mana - cost
                nextcost = costnow + cost
                nexttimers = list(timers)
                nextHP = HP
                nextboss_HP = boss_HP
                if i==0:
                    nextboss_HP = nextboss_HP - 4
                if i==1:
                    nextboss_HP = nextboss_HP - 2
                    nextHP = nextHP + 2
                if i>=2 and nexttimers[i-2]==0:
                    nexttimers[i-2] += 6 - (i==4) # 6, 6, 5 turns depending on i
                if nextboss_HP <= 0:
                    if nextcost < bestcost:
                        bestcost = nextcost
                    # no further paths from here
                    continue

                # now let boss attack in the same subpath, for simplicity
                nexttimers,nextboss_HP,nextmana,defense = step_effects(nexttimers, nextboss_HP, nextmana)
                if nextboss_HP <= 0:
                    if nextcost < bestcost:
                        bestcost = nextcost
                    # no further paths from here
                    continue
                nextHP -= max(boss_att - defense,1)
                if nextHP <= 0:
                    # we're dead
                    continue

                # if we're here: both we and boss survived a player/boss turn pair
                if nextcost > bestcost:
                    # give up on this path for the record
                    continue

                # now we need to go on in the next BFS turn
                newpaths.append({'costnow': nextcost, 'HPs': (nextHP, nextboss_HP), 'mana': nextmana, 'timers': nexttimers})
            # done spawning new paths from a single original path
        # done with all the original paths
        oldpaths = newpaths
        # and we're set for a new BFS iteration
   
def step_effects(timers, boss_HP, mana):
    if timers[0] > 0:
        defense = 7
        timers[0] -= 1
    else:
        defense = 0
    if timers[1] > 0:
        boss_HP = boss_HP- 3
        timers[1] -= 1
    if timers[2] > 0:
        mana = mana + 101
        timers[2] -= 1
    return timers, boss_HP, mana, defense
    # yes, returning timers is redundant

if __name__ == "__main__":
    inps = open('day22.inp').read()
    print(day22(inps))
    print(day22(inps, part2=True))
