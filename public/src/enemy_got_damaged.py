import random 
from colors import color_yellow
def enemy_got_damaged_events(champion,enemy):
    stun_chance = random.randint(0,100) <= 50
    print("enemy got damaged")
    if champion.thunderbrand_buff > 0:
        if stun_chance:
            print(color_yellow(f"Thunder crashes as you hit {enemy.name}, stunning them with its unstoppable force!"))
            enemy.cc_status = "stunned"

