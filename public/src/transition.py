from fight import fight
from races import *
from game_classes import *
from store import store
from colors import color_red
from won_fight import needed_xp
from xp_for_levels import max_level


#champion = Thief(Troll())
def print_general_stats(champion):
    print(f"Combat stats: {int(champion.hp)}/{champion.totalhp} HP || attack: {int(champion.dummy_attack)} || defense: {int(champion.dummy_defence)}")
    print(f"° LEVEL: {champion.level}")
    print(f"° You have {champion.total_coins} coins ",end="||")
    if champion.level < max_level:
        print(f" XP {champion.total_xp}/{needed_xp[champion.level]}")
    else:
        print(" MAX LEVEL REACHED ∞/00")
    print(f"° You have {champion.consumables["Hank"][0]} Hanks")
    print("\n")


def transiction_phase(champion):
    print_general_stats(champion)
    to_do_list = ["Store","Fight","Fight Boss"]
    for index,action in enumerate(to_do_list,1):
        if champion.level < max_level and action == "Fight Boss":
            continue
        print(f"{index}. {action}")
    to_do = input("""What do you want to do?
                  --> """).lower().strip()
    print("\n")
    
    match to_do:
        case "fight":
            fight(champion)
        case "store":
            store(champion)
        case "fight boss":
            fight(champion,True)
        case _:
            print(f"{color_red("Such action dont exists")}")
            return transiction_phase(champion)
        
    
    

    
    


    
    

#transiction_phase()

