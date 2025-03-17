from colors import color_green
from xp_for_levels import needed_xp
import random
from colors import color_green
from start_turn_e import hp_checker

def check_hasattr_resources(champion,resource):
    if hasattr(champion,resource):
        return True



def lvl_multiplier(champion):
    main_stat = getattr(champion,"main_stat")
    str_mul = champion.strength * champion.level
    agi_mul = champion.agility * champion.level
    int_mul = champion.intellect *champion.level
    if main_stat == "str":
        champion.totalhp += 20 * str_mul
        champion.dummy_attack += 2 * str_mul
        champion.dummy_defence += (2 * str_mul) + agi_mul
        champion.hp += 20 * str_mul
    elif main_stat == "agi":
        champion.totalhp += 12 * str_mul
        champion.hp += 12 * str_mul
        champion.dummy_attack += 5 * agi_mul
    elif main_stat == "int":
        champion.totalhp += 5 * str_mul
        champion.hp += 5 * str_mul
        champion.dummy_attack += 4 * int_mul
        champion.totalmana += 20 * int_mul

def get_loot(champion,enemy):
    lootable_items = list(champion.consumables.keys())[:-1]
    random_num = random.randint(0,100)
    #print(lootable_items)
    if random_num < enemy.loot_chance:
        random_item = random.randint(0,len(lootable_items)-1)
        loot = lootable_items[random_item]
        champion.consumables[loot][0] += 1
        print(color_green(f"You found a {loot} in {enemy.name}'s dead body."))


def won_fight(champion,enemy):
    champion.total_coins += enemy.give_coins
    print(f"You gain {enemy.give_coins} coins")
    
    if champion.level < 5:
        champion.total_xp += enemy.give_xp
        print(f"You gain {enemy.give_xp} XP")
        if champion.total_xp >= needed_xp[champion.level]:
            champion.level += 1
            print(color_green(f"LEVEL UP!!! you are now level : {champion.level}"))
            lvl_multiplier(champion)
            champion.total_xp -= needed_xp[champion.level-1]
    
    print(color_green("You won the fight! and all your cooldowns are available again"))
    get_loot(champion,enemy)
    print("\n")


    
    if check_hasattr_resources(champion,"energy"):
        champion.energy = champion.totalenergy
    if check_hasattr_resources(champion,"mana"):
        champion.mana = champion.totalmana

    #champion.hp += (champion.totalhp/100) * 10
    hp_checker(champion)

    all_attrs = dir(champion)
    durations_list = []
    for duration in all_attrs:
        if duration.endswith("_duration"):
            durations_list.append(duration)
    for attr in durations_list:
        setattr(champion,attr,0)
    for player_buffs in all_attrs:
        if player_buffs.endswith("_buff") or player_buffs.endswith("_dot"):
            setattr(champion,player_buffs,0)

    enemy.cc_status = "ok"
    enemy.hp = enemy.totalhp
    all_enemy_attrs = dir(enemy)
    for dot in all_enemy_attrs:
        if dot.endswith("_dot"):
            setattr(enemy,dot,0)






