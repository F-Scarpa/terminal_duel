from races import *
from game_classes import *
from colors import color_red

# general
def first_aid_cd(champion):
    if champion.first_aid_duration > 0:
        champion.first_aid_duration -= 1

#warrior
def warrior_spirit_cd(champion):
    if champion.warrior_spirit_duration > 0:
        champion.warrior_spirit_duration -= 1

def berserker_rage_cd(champion):
    if champion.berserker_rage_duration > 0:
        champion.berserker_rage_duration -= 1



#mage
def frost_shards_cd(champion):
    if champion.frost_shards_duration > 0:
        champion.frost_shards_duration -= 1
def rewind_time_cd(champion):
    if champion.rewind_time_duration > 0:
        champion.rewind_time_duration -= 1

def stop_time_cd(champion):
    if champion.stop_time_duration > 0:
        champion.stop_time_duration -= 1

#thief
def shadowstep_cd(champion):
    if champion.shadowstep_duration > 0:
        champion.shadowstep_duration -= 1 


def cd_tracker(champion):
    first_aid_cd(champion)

    if champion.game_class == "warrior":
        warrior_spirit_cd(champion)
        berserker_rage_cd(champion)

    if champion.game_class == "mage":
        frost_shards_cd(champion)
        stop_time_cd(champion)
        rewind_time_cd(champion)
    
    if champion.game_class == "thief":
        shadowstep_cd(champion)

    

__names_list = []
def create_spell_names_list(champion):
    cooldowns = dir(champion)
    spell_names = list(filter(lambda spell:spell.startswith("spell_") and spell.endswith("_cd"),cooldowns))
    for spell in spell_names:
        spell = spell.replace("_"," ")[6:-3]
        __names_list.append(spell)


#champion = Warrior(Troll())

def cd_printer(champion):

    cooldowns = dir(champion)
    spell_list = list(filter(lambda spell:not spell.startswith("spell_") and spell.endswith("_duration"),cooldowns))
    for spell in spell_list:
        actual_cd = getattr(champion,spell)
        #print(spell)
        keyword = spell[:-9].replace("_"," ")
        #print(f"deve essere uguale a names_list : {keyword}")
        #print(actual_cd)
        if actual_cd > 0:
            if keyword in __names_list:
                print(f"{keyword.title()} still have {color_red(f"{actual_cd} turns cd")}")

        
    

    
"""print("names_list:")
create_spell_names_list(champion)
print(__names_list)"""
#create_spell_names_list(champion)
#cd_printer(champion)


                
            



            


            
            
    
