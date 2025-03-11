import random
from colors import color_red
class Enemy:
    def __init__(self,name,hp,atk,defe,give_xp,give_coins,loot_chance):
        # stats
        self.name = name
        self.totalhp = hp
        self.hp = hp
        self.atk = atk
        self.defe = defe
        #reward on kill
        self.give_xp = give_xp
        self.give_coins = give_coins
        self.loot_chance = loot_chance
        # debuff trackers
        #warrior dot
        self.deep_cut_dot = 0
        # mage dot
        self.fireball_dot = 0
        # mage cc
        self.stop_time_cc = 0
        self.frozenhp = 0
        self.cc_status = "ok"
        #thief cc
        self.shadowstep_cc = 0

    def attack(self,champion):
        if self.cc_status == "ok":
            damage = self.atk - champion.defence
            if damage <= 0:
                damage = 1
                champion.hp -= 1
            else:
                champion.hp -= damage
            print(f"\033[91m{self.name} hit you for {damage}, you have {int(champion.hp)}/{champion.totalhp} hp left\033[0m")

 
enemy_names = [
    "Thug", "Mercenary", "Assassin", "Rogue", "Brigand", "Outlaw", "Smuggler", "Raider",
    "Warlord", "Marauder", "Cutthroat", "Highwayman", "Corsair", "Berserker", "Enforcer",
    "Slaver", "Bandit Leader", "Dark Knight", "Shadowblade", "Cultist", "Warlock", "Duelist",
    "Hunter", "Gladiator", "Prowler", "Knight Errant", "Bounty Hunter", "Reaver", "Infiltrator",
    "Sharpshooter"
]
        

enemies = []

def create_enemy(name,hp,atk,defe,give_xp,give_coins = 5,loot_chance = 10):
    enemy = Enemy(name.title(),hp,atk,defe,give_xp,give_coins,loot_chance)
    enemies.append(enemy)

def select_enemy():
    enemy = random.choice(enemies)
    print(color_red(f"{enemy.name} want to fight you!"))
    return enemy

for name in enemy_names:
    hp = random.randint(2000, 4000)
    atk = random.randint(20, 30)
    defe = random.randint(5, 20)
    give_xp = random.randint(10, 20)  # Esperienza casuale tra 10 e 50
    give_coins = random.randint(3, 15)  # Monete casuali tra 3 e 15

    create_enemy(name, hp, atk, defe, give_xp, give_coins)

final_boss = Enemy("Boss",1000,50,30,0,0,0)

#enemy = select_enemy()







