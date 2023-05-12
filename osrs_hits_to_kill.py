# average number of hit to kill calc. use dps calc for other numbers
import random

def proc_chance(bolts, diary):
    if bolts is None:
        return 0

    d = {
        "ruby": .11,
        "diamond": .1
    }
    chance = d[bolts]
    if diary:
        chance = chance*1.1
    return chance

def bolt_dmg(max_hit, curr_hp, bolts):
    d = {
        "ruby": min(100, int(curr_hp*.2)),
        "diamond": int(random.random()*(max_hit*1.15+1))
    }
    return d[bolts]

def ticks_to_kill(hp, accuracy, max_hit, speed, bolts=None, diary=True):
    curr_hp = hp
    num_ticks = 0

    while curr_hp > 0:
        num_ticks += speed

        chance = proc_chance(bolts, diary)
        bolt_proc = (chance > random.random())
        if bolt_proc:
            curr_hp -= bolt_dmg(max_hit, curr_hp, bolts)
            continue

        hit = (accuracy > random.random())
        if not hit:
            continue

        curr_hp -= int(random.random()*(max_hit+1))
    
    return num_ticks

# brutal black dragons dhcb ruby vs diamond
hp = 315
accuracy = 0.7
max_hit = 57
weapon_speed = 5

sum1 = 0
for i in range(0, 1000):
    sum1 += ticks_to_kill(hp, accuracy, max_hit, weapon_speed, bolts="ruby")

sum2 = 0
for i in range(0, 1000):
    sum2 += ticks_to_kill(hp, accuracy, max_hit, weapon_speed, bolts="diamond")

# ruby slightly worse
print(sum1/1000)
print(sum2/1000)
