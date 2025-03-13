from races import Races
from colors import *
from start_turn_e import full_check
import random, time
import sys

def no_mana_message(champion):
    print(f"{color_red(f"Not enough mana, you have {champion.mana} and {champion.mana_cost} is needed")}")
    return "no mana"

def no_energy_message(champion,energy_cost):
    print(f"{color_red(f"Not enough energy, you have {champion.energy} and {energy_cost} is needed")}")
    return "no energy"


# Action every class have in common
class CommonActions():
    def __init__(self):
        self.total_xp = 0
        self.level = 1
        self.total_coins = 20 + 99999
        self.first_aid_duration = 0

        #general buffs
        self.vampiric_aegis_buff = 0
        self.thunderbrand_buff = 0

        #starting items count
        self.hank_num = 1
        self.heal_pot_num = 0
        self.fire_candy_num = 0
        self.soulpiercer_dagger_num = 0
        self.vampiric_aegis_num = 0
        self.thunderbrand_num = 1

        #items => name:[num,description,cost]
        self.consumables = {
                       "Healing Potion":[self.heal_pot_num,"Heal yourself for 50% total hp",15],
                       "Thunderbrand":[self.thunderbrand_num,"Gives you a 50% chance to stun the enemy on hit for 1 turn in the next 4 turns",30],
                       "Fire Candy":[self.fire_candy_num,"Deals 100 damage to the enemy",10],
                       "Soulpiercer Dagger":[self.soulpiercer_dagger_num,"Steal hp from the enemy",35],
                       "Vampiric Aegis":[self.vampiric_aegis_num,"For the next 2 turns 10% of the damage will heal you instead",25],
                       "Hank":[self.hank_num,"You fully regain your HP after dying.",100]
                       }
    def is_defeated(self,champion):
        if self.hank_num > 0:
            champion.hp = champion.totalhp
            self.hank_num -= 1
            print(color_green(f"You died but you used one hank, you're back to full hp and have {color_cyan(f'{self.hank_num} more hanks')}"))
            
            return False
        else:
            print(f"{color_red('Your hp reached 0, you lost =(')}")
            sys.exit()
            
        
    def spell_inventory(self,champion,target):
        #items
        def vampiric_aegis(self,target):
            # check if item is available
            if self.consumables["Vampiric Aegis"][0] > 0:
                self.consumables["Vampiric Aegis"][0] -= 1
                # logic
                self.vampiric_aegis_buff = 2

                # print usefull info about what happens
                print(f"You use a vampiric aegis to defend yourself!")
                print(f"you now have {self.consumables["Vampiric Aegis"][0]} Vampiric Aegis")
            # when you dont have anymore of the selected item
            else:
                print(f"{color_red("You have no Vampiric Aegis left")}")
                return self.spell_inventory(champion,target)
            return self.vampiric_aegis_num
        #end////////////////////////////////////////

        def thunderbrand(self):
            # check if item is available
            if self.consumables["Thunderbrand"][0] > 0:
                self.consumables["Thunderbrand"][0] -= 1
                # logic
                self.thunderbrand_buff = 4

                # print usefull info about what happens
                print(color_cyan("You break a magical seal, unleashing the power of thunder within you!"))
                print(f"You now have {self.consumables["Thunderbrand"][0]} Thunderbrands")
            # when you dont have anymore of the selected item
            else:
                print(f"{color_red("You have no Thunderbrands left")}")
                return self.spell_inventory(champion,target)
            return self.thunderbrand_num
        #end////////////////////////////////////////


        def soulpiercer_dagger(self,target):
            # check if item is available
            if self.consumables["Soulpiercer Dagger"][0] > 0:
                self.consumables["Soulpiercer Dagger"][0] -= 1
                # logic
                damage = ((champion.totalhp / 100) *20) - target.defe
                target.hp = target.hp - damage 
                champion.hp += damage

                # print usefull info about what happens
                print(f"You throw a cursed dagger against {target.name}, stealing {color_red(int(damage))} health")
                print(f"you now have {self.consumables["Soulpiercer Dagger"][0]} soulpiercer daggers")
            # when you dont have anymore of the selected item
            else:
                print(f"{color_red("You have no soulpiercer daggers left")}")
                return self.spell_inventory(champion,target)
            return self.soulpiercer_dagger_num
        #end////////////////////////////////////////

        def fire_candy(self,target):
            if self.consumables["Fire Candy"][0] > 0:
                self.consumables["Fire Candy"][0] -= 1
                damage = 100
                target.hp = target.hp - damage 
                print(f"You breath fire against {target.name}, dealing {color_red(damage)} damage")
                print(f"you now have {self.consumables["Fire Candy"][0]} fire candies")
            else:
                print(f"{color_red("You have no fire candies left")}")
                return self.spell_inventory(champion,target)
            return self.fire_candy_num
        
        def healing_potion(self):
            if self.consumables["Healing Potion"][0] > 0:
                self.consumables["Healing Potion"][0] -= 1
                heal = (champion.totalhp/100) * 50
                champion.hp += heal
                print(color_green(f"You heal yourself for {heal} hp"))
                print(f"You now have {self.consumables["Healing Potion"][0]} healing potions")

            else:
                print(color_red("You have no healing potions left"))
                return self.spell_inventory(champion,target)
            return self.heal_pot_num


        # do not touch
        self.spell_name = "check inventory"
        self.spell_description = ""
        for item in self.consumables:
            if item == "Hank":
                continue
            print(f"{item} | quantity: {self.consumables[item][0]} --> {self.consumables[item][1]}")
        print("Back")
        print("\n")
        use = input("""Which item do you want to use?
                    --> """).title().strip()
        
        match use:
            case "Back":
                return "back_try"
            case "Soulpiercer Dagger":
                return soulpiercer_dagger(self,target)
            case "Thunderbrand":
                return thunderbrand(self)
            case "Vampiric Aegis":
                return vampiric_aegis(self,target)
            case "Healing Potion":
                return healing_potion(self)
            case "Fire Candy":
                return fire_candy(self,target)
            case "You dont have any more of that item":
                return "back_try"
            case _:
                print(color_red("That item dont exists"))
                return self.spell_inventory(champion,target)
    spell_inventory.spell_name = "Check Inventory"
    spell_inventory.spell_description = "Check your inventory"

 
    def spell_first_aid_cd(self):
        self.spell_name = "first aid"
        self.spell_description = ""
        if self.first_aid_duration == 0:
            heal = (self.totalhp/100) * 15
            self.hp += heal
            self.first_aid_duration = 8
            print(f"\033[32mYou heal yourself with {self.spell_name} for {heal} hp\033[0m") 
        else:
            print(f"{self.spell_name} still have {self.first_aid_duration} turns duration")

    spell_first_aid_cd.spell_name = "First Aid"
    spell_first_aid_cd.spell_description = f"Heal yourself for 15% of your total hp || {color_cyan("no cost / 8 turns cooldown")}"

    def spell_pass(self,champion,target,dummy):
        sentences = ["You do absolutely nothing... and somehow, it feels strategic.",
                     "You stare at the enemy menacingly. They are unimpressed.",
                     "You take a deep breath... maybe next turn will be your moment!",
                     "You pretend this was all part of a master plan.",
                     "You pass your turn. The enemy sighs in relief."]
        all_sentences = len(sentences)
        random_sentence = random.choice(sentences)
        spell_name = ""
        spell_description = ""
        champion.hp += (champion.totalhp/100) * 10
        if hasattr(champion,"energy"):
            champion.energy += (champion.totalenergy/100) * 10
        if hasattr(champion,"mana"):
            champion.mana += (champion.totalmana/100) * 10
        #full check
        full_check(self)
        print(random_sentence)
        
    spell_pass.spell_name = "Pass"
    spell_pass.spell_description = "Wait and do nothing for this turn, regenerate 10% hp and 10% of your resources"


# Playable classes
class Warrior(Races,CommonActions):
    def __init__(self,race_node):
        CommonActions.__init__(self)
        self.totalhp = 20 * race_node.stre
        self.hp = 20 * race_node.stre
        self.dummy_attack = 2 * race_node.stre
        self.dummy_defence = (2 * race_node.stre) + race_node.agi
        self.attack = 2 * race_node.stre
        self.defence = (2 * race_node.stre) + race_node.agi
        self.race = race_node.race
        self.game_class = "warrior"
        #multipliers
        self.main_stat = "str"
        self.strength = 3
        self.agility = 1
        self.intellect = 1
        # durations
        self.warrior_spirit_duration = 0
        self.berserker_rage_duration = 0
        #buffs
        self.warrior_spirit_buff = 0
        self.berserker_rage_buff = 0
        self.sundering_strike_buff = 0
        self.sundering_strike_used_last_turn = False
        self.SS_stack = 0


    def spell_sundering_strike(self,target):
        self.spell_name = ""
        self.spell_description = ""
        damage = self.attack - target.defe + (self.SS_stack * self.attack)
        target.hp -= damage
        if damage <= 0:
            damage = 1
        self.sundering_strike_buff = 2
        self.sundering_strike_used_last_turn = True
        self.SS_stack += 1
        print(color_yellow(f"You hit {target.name} for {damage} damage"))

    spell_sundering_strike.spell_name = "Sundering Strike"
    spell_sundering_strike.spell_description = "Deals incrementing damage with each subsequent use but spell's damage turns back to it's original value if another action other than Sundering Strike is taken"



    def spell_piercing_strike(self,target):
        #print("spell_piercing_strike CALLED!")
        self.spell_name = "piercing strike"
        self.spell_description = ""
        self.damage = self.attack
        target.hp -= self.damage
        print(f"\033[93mYou hit {target.name} with {self.spell_name} for {self.damage} damage\033[0m")
        
    spell_piercing_strike.spell_name = "Piercing Strike"
    spell_piercing_strike.spell_description = f"Hit the target dealing damage and ignoring defenses || {color_cyan('no cost')}"

    def spell_deep_cut(self,target):
        self.spell_name = "deep cut"
        self.spell_description = ""
        self.damage = ((self.attack // 2) + 2) - target.defe
        if self.damage < 0:
            self.damage = 1
        target.hp -= self.damage
        target.deep_cut_dot = 5 
        print(f"\033[93mYou hit {target.name} with deep cut for {self.damage} damage\033[0m")
        
    spell_deep_cut.spell_name = "Deep Cut"
    spell_deep_cut.spell_description = f"Deals istant damage and damage over time for the next 5 turns || {color_cyan("no cost")}"


    def spell_warrior_spirit_cd(self,target):
        self.spell_name = "warrior spirit"
        self.spell_description = ""
        # duration is a cd tracker
        self.warrior_spirit_duration = 10
        self.warrior_spirit_buff = 5
        print("You gain 50 bonus attack damage and defense for 5 turns")

    spell_warrior_spirit_cd.spell_name = "Warrior Spirit"
    spell_warrior_spirit_cd.spell_description = f"Increase your attack and defence by 50 points || {color_cyan("no cost / 10 turns cooldown")}"

    def spell_berserker_rage_cd(self,target):
        spell_name = ""
        spell_description = ""
        #duration is a cd tracker
        self.berserker_rage_duration = 10
        # _buff is the ampunt of turns the spell will be active
        self.berserker_rage_buff = 7
        self.defence = 0
        print(color_cyan("Fueled by rage, you attack relentlessly, casting aside your own safety!"))

    spell_berserker_rage_cd.spell_name = "Berserker Rage"
    spell_berserker_rage_cd.spell_description = f"Doubles your attack but reduce your defenses to 0 and connot benefit from defenses bonuses || {color_cyan("no cost / 10 turns cooldown")}"


    

    def __repr__(self):
        return f"hp:{self.hp} / attack:{self.attack} / defence:{self.defence}"
    
class Mage(Races,CommonActions):
    def __init__(self,race_node):
        CommonActions.__init__(self)
        self.totalhp = 15 * race_node.stre
        self.hp = 15 * race_node.stre
        self.dummy_attack = 4 * race_node.inte
        self.dummy_defence = race_node.stre // 2
        self.attack = 4 * race_node.inte
        self.defence = race_node.stre // 2
        self.totalmana = 20 * race_node.inte
        self.mana = 20 * race_node.inte
        self.race = race_node.race
        self.game_class = "mage"
        #multipliers
        self.main_stat = "int"
        self.strength = 1
        self.agility = 1
        self.intellect = 3
        #durations
        self.frost_shards_duration = 0
        self.stop_time_duration = 0

    def spell_frost_shards_cd(self,target):
        self.spell_name = "frost shards"
        self.spell_description = ""
        self.mana_cost = 35

        if self.mana >= self.mana_cost:
            self.mana -= self.mana_cost
            self.frost_shards_duration = 5
            total_damage = 0
            for i in range(3):
                dice = random.randint(0,self.attack)
                total_damage += (self.attack + dice) - target.defe
                if total_damage < 0:
                    total_damage = 1
                print(f"{color_yellow(f"You hit {target.name} for {(self.attack + dice) - target.defe} damage")}")
                time.sleep(0.5)
            target.hp -= total_damage
            print(f"\033[93mYour frost shards damaged {target.name} for a total of {total_damage} damage\033[0m")
        else:
            print(f"{color_red(f"Not enough mana, you have {self.mana} and {self.mana_cost} is needed")}")
            return "no mana"
    
    spell_frost_shards_cd.mana_cost = 35
    spell_frost_shards_cd.spell_name = "Frost Shards"
    spell_frost_shards_cd.spell_description = f"Throw 3 frost shards at the enemy || {color_cyan(f"{spell_frost_shards_cd.mana_cost} mana / 5 turns cooldown" )}"

    def spell_fireball(self,target):
        spell_name = "Fireball"
        spell_description = ""
        self.mana_cost = 20
        damage = self.attack - target.defe
        if self.mana >= self.mana_cost:
            self.mana -= 20
            target.hp -= damage
            target.fireball_dot = 3
            print(f"{color_yellow(f"Fireball deals {damage} damage to {target.name}")}")
        else:
            return no_mana_message(self)
    spell_fireball.mana_cost = 20
    spell_fireball.spell_name ="Fireball"
    spell_fireball.spell_description = f"Hurls a fireball to the enemy dealing istant damage and damage over the next 3 turns || {color_cyan(f"{spell_fireball.mana_cost} mana ")}"

    def spell_stop_time_cd(self,target):
        spell_name = ""
        spell_description = ""
        self.mana_cost = 80
        if self.mana >= self.mana_cost:
            self.mana -= self.mana_cost
            self.stop_time_duration = 8
            target.frozenhp = target.hp
            target.stop_time_cc = 3
            print(color_yellow("You have frozen the enemy in time"))
        else:
            return no_mana_message(self)
    spell_stop_time_cd.mana_cost = 80
    spell_stop_time_cd.spell_name = "Stop Time"
    spell_stop_time_cd.spell_description = f"Freeze the enemy in time for the next 3 turns, the effect will end if the enemy is damaged || {color_cyan(f"{spell_stop_time_cd.mana_cost} mana / 8 turns cooldown")}"



    def __repr__(self):
        return f"hp:{self.hp} / mana:{self.mana} / attack:{self.attack} / defence:{self.defence}"
    
class Thief(Races,CommonActions):
    def __init__(self,race_node):
        CommonActions.__init__(self)
        #stats
        self.totalhp = 12 * race_node.stre
        self.hp = 12 * race_node.stre
        self.dummy_defence = race_node.agi
        self.dummy_attack = 5 * race_node.agi
        self.attack = 5 * race_node.agi
        self.defence = race_node.agi
        self.race = race_node.race
        self.game_class = "thief"
        #resources
        self.cp = 0
        self.totalcp = 5
        self.totalenergy = 100
        self.energy = 100
        #multipliers
        self.main_stat = "agi"
        self.strength = 1
        self.agility = 3
        self.intellect = 1
        #duration
        self.shadowstep_duration = 0
        self.shadowstep_buff = False

    def spell_eviscerate(self,target):
        self.spell_name = ""
        self.spell_description = ""

        damage = self.attack - target.defe

        if self.cp == 0:
            print(color_red("This ability requires atleast 1 cp"))
            return "no cp"
        else:
            match self.cp:
                case 1:
                    damage *= 0.25
                case 2:
                    damage *= 0.6
                case 3:
                    damage *= 1
                case 4:
                    damage *= 2.5
                case 5:
                    damage *= 6

            target.hp -= int(damage)
            self.cp = 0
            print(color_yellow(f"You hit {target.name} for {int(damage)} damage"))
    
    
    spell_eviscerate.spell_name = "Eviscerate"
    spell_eviscerate.spell_description = f"Deal istant damage increasing by combo points. || {color_cyan(f"Requires atleast 1 combo point")}"

    def spell_shadowstep_cd(self,target):
        spell_name = ""
        spell_description = ""
        energy_cost = 20
        if energy_cost < self.energy:
            self.energy -= 20
            self.shadowstep_duration = 4
            target.shadowstep_cc = 1
            self.shadowstep_buff = True
        else:
            return no_energy_message(self,energy_cost)
    spell_shadowstep_cd.energy_cost = 20
    spell_shadowstep_cd.spell_name = "Shadowstep"
    spell_shadowstep_cd.spell_description = f"Stun the target for the next turn and empower your next damaging ability. || {color_cyan(f"{spell_shadowstep_cd.energy_cost} energy / 4 turns cooldown")}"



    def spell_swift_strike(self,target):
        spell_name = ""
        spell_description = ""
        energy_cost = 30
        if energy_cost < self.energy:
            self.energy -= energy_cost
            damage = (int(self.attack * 1.4)) - target.defe
            if target.hp == target.totalhp:
                damage = int(damage * 2 )
                self.cp += 1

            target.hp -= damage
            self.cp += 1
            print(color_yellow(f"You hit {target.name} for {damage} damage"))
        else:
            return no_energy_message(self,energy_cost)

    spell_swift_strike.energy_cost = 30
    spell_swift_strike.spell_name = "Swift Strike"
    spell_swift_strike.spell_description = f"Hits the target, dealing instant damage. If the target is at full health, the damage is doubled. || {color_cyan(f"{spell_swift_strike.energy_cost} energy")}"


    def __repr__(self):
        return f"hp:{self.hp} / energy:{self.energy} / attack:{self.attack} / defence:{self.defence}"
    

