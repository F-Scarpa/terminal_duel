from colors import color_cyan, color_yellow

def print_enemy_status(target):
    print(f"\033[93m{target.name} have {target.hp}/{target.totalhp} hp left.\033[0m")

def print_champion_status(champion):
    print(f"\033[32mYou have {champion.hp}/{champion.totalhp} hp left\033[0m")

#hp
def hp_checker(champion):
    if champion.hp > champion.totalhp:
        champion.hp = champion.totalhp

#mage
def mana_checker(champion):
    if champion.mana > champion.totalmana:
        champion.mana = champion.totalmana
#resources
#thief
def energy_checker(champion):
    if champion.energy > champion.totalenergy:
        champion.energy = champion.totalenergy
def cp_checker(champion):
    if champion.cp > champion.totalcp:
        champion.cp = champion.totalcp

#items durations buffs
def check_vampiric_aegis(champion):
    if champion.vampiric_aegis_buff > 0:
        champion.vampiric_aegis_buff -= 1
        print(color_cyan(f"Vampiric aegis buff will last {champion.vampiric_aegis_buff} more turns"))

def check_thunderbrand(champion):
    if champion.thunderbrand_buff > 0:
        champion.thunderbrand_buff -= 1
        print(color_cyan(f"Thunderbrand buff will last {champion.thunderbrand_buff} more turns"))


#warrior buffs
def check_warrior_spirit_buff_remaining(champion):
    if getattr(champion,"warrior_spirit_buff") > 0:
         champion.warrior_spirit_buff -= 1
         print(color_cyan(f"Warrior's Spirit will last for {champion.warrior_spirit_buff} more turns"))

def check_sundering_strike_buff_remaining(champion):
    if getattr(champion,"sundering_strike_buff") > 0:
         champion.sundering_strike_buff -= 1
    if (getattr(champion,"sundering_strike_buff") == 0 
          and getattr(champion,"sundering_strike_used_last_turn") is True):
        champion.sundering_strike_used_last_turn = False
        champion.SS_stack = 0

def check_berserker_rage_buff_remaining(champion):
    if getattr(champion,"berserker_rage_buff") > 0:
         champion.berserker_rage_buff -= 1
         print(color_cyan(f"Berserker's Rage will last for {champion.berserker_rage_buff} more turns"))
    
#mage buffs
def check_rewind_time_buff_remaining(champion):
    if getattr(champion,"rewind_time_buff") > 0:
         champion.rewind_time_buff -= 1
         if champion.rewind_time > 0:
            print(color_cyan(f"Rewind time will activate after {champion.rewind_time_buff} turns"))
         else:
            print(color_cyan(f"Rewind time activated!").upper())
    if champion.rewind_time_buff == 0 and champion.rewind_time_is_active:
        champion.hp = champion.rewind_time_hp
        champion.mana = champion.rewind_time_mana
        champion.rewind_time_is_active = False

def check_paralyzing_knife_dot_duration(champion,enemy):
    if champion.paralyzing_knife_dot > 0:
        champion.paralyzing_knife_dot -= 1
        damage = champion.total_PK_damage // 5
        if damage <= 1:
            damage = 1
        enemy.hp -= damage
        print(color_yellow(f"{enemy.name} suffers {int(damage)} damage"))


    

#full buff check
def check_all_buffs(champion,enemy):
     #items
     check_vampiric_aegis(champion)
     check_thunderbrand(champion)
     #warrior
     if champion.game_class == "warrior":
        check_warrior_spirit_buff_remaining(champion)
        check_berserker_rage_buff_remaining(champion)
        check_sundering_strike_buff_remaining(champion)
     if champion.game_class == "mage":
         check_rewind_time_buff_remaining(champion)
     if champion.game_class == "thief":
         check_paralyzing_knife_dot_duration(champion,enemy)

    


#full check
def full_check(champion):
    hp_checker(champion)
    
    if hasattr(champion,"mana"):
        mana_checker(champion)
        print(color_cyan(f"You have {int(champion.mana)}/{champion.totalmana} mana"))

    if hasattr(champion,"energy"):
        energy_checker(champion)
        print(color_cyan(f"You have {int(champion.energy)}/{champion.totalenergy} energy"))
    if hasattr(champion,"cp"):
        cp_checker(champion)
        print(color_cyan(f"You have {int(champion.cp)}/{champion.totalcp} combo points"))




def start_turn_events(champion,enemy):
    # resources regeneration
    if hasattr(champion,"mana"):
        mana_regen = (champion.totalhp/100) * 5
        champion.mana += mana_regen
    if hasattr(champion,"energy"):
        energy_regen = (champion.agility * 3) + champion.level
        champion.energy += energy_regen

    # racial bonuses
    if champion.race == "troll":
        hp_regen = (champion.totalhp/100) * 3
        champion.hp += hp_regen
        print("\033[32mTrolls regenerates 3% of their total hp every turn\033[0m")
    if champion.race == "gnome" and hasattr(champion,"mana"):
        mana_regen = (champion.totalhp/100) * 5
        champion.mana += mana_regen

    #full check
    check_all_buffs(champion,enemy)
    full_check(champion)
    champion.hp = int(champion.hp)
    champion.totalhp = int(champion.totalhp)
    enemy.hp = int(enemy.hp)
    enemy.totalhp = int(enemy.totalhp)
    print_champion_status(champion)
    print_enemy_status(enemy)
    enemy.cc_status = "ok"

    



