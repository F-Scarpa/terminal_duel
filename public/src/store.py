from colors import color_red
from game_classes import CommonActions,Warrior,Thief,Mage
from races import Gnome,Troll,Orc,Human
from colors import color_red, color_green, color_cyan





def store(champion):
    from transition import transiction_phase
    consumables = CommonActions()
    items_to_buy = consumables.consumables
    #print(items_to_buy)

    def buy_item(champion,item):
        item_cost = items_to_buy[item][2]
        quantity = items_to_buy[item][0]
        if item in items_to_buy:
            if champion.total_coins >= item_cost:
                champion.total_coins -= item_cost
                champion.consumables[item][0] += 1
                print(f"{color_green(f"You bought {item} successfully for {champion.consumables[item][2]} coins")}")

            else:
                print(f"{color_red(f"You dont have enough coins {item} costs {items_to_buy[item][2]} coins and you have {champion.total_coins}")}")
            return store(champion)
            
        else:
            print("That item doesnt exists")
    
    
    

    print(f"{color_cyan(f"""You have {champion.total_coins} coins left\nAvailable Items:""")}")
    for item in items_to_buy:
        print(f"Buy {item} --> {items_to_buy[item][1]} || COST: {items_to_buy[item][2]} coins || you currently have {champion.consumables[item][0]} {item}s")
    print("Back")
    print("\n")
    to_buy = input("""Type the item you like to buy
                   --> """).title().strip()
    
    # add the buying option for every purchaseable item
    match to_buy:
        case "Healing Potion":
            buy_item(champion,to_buy)
        case "Vampiric Aegis":
            buy_item(champion,to_buy)
        case "Soulpiercer Dagger":
            buy_item(champion,to_buy)
        case "Thunderbrand":
            buy_item(champion,to_buy)
        case "Fire Candy":
            buy_item(champion,to_buy)
        case "Hank":
            buy_item(champion,to_buy)
        
        case "Back":
            return transiction_phase(champion)

        case _:
            print(f"{color_red("The item you typed doesnt exists")}")
            return store(champion)
        


