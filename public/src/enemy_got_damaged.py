import random 
from colors import color_yellow
def enemy_got_damaged_events(champion,enemy):
    #thunderbrand item
    if champion.thunderbrand_buff > 0:
        stun_chance = random.randint(0,100) <= 50
        if stun_chance:
            print(color_yellow(f"Thunder crashes as you hit {enemy.name}, stunning them with its unstoppable force!"))
            enemy.hp -= 35
            enemy.cc_status = "stunned"
    
    if champion.game_class == "thief":
        if champion.shadowstep_buff:
            champion.shadowstep_buff = False

