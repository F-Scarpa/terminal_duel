from races import Human, Gnome, Orc, Troll
from game_classes import Warrior,Mage,Thief

def create_character():
    selected_race = ""
    race_selection = True
    while race_selection == True:
        choosen_race = input('''Type the race you like to play :
                            1.Human => Human have higher base stats (suggested class: any)
                            2.Gnome => Gnomes regenerates double amount of mana(suggested class: mage)
                            3.Orc => Orcs deals bonus damage when their health is under 50% (suggested class: warrior)
                            4.Troll => Trolls regenerates 3% of their health every turn (suggested class: thief)
                            
                            Your choice --> ''').lower().strip()

        race_selection = False
        race = None
        selected_race = choosen_race
        match (choosen_race):
            case "human":
                race = Human()
            case "gnome":
                race = Gnome()
            case "orc":
                race = Orc()
            case "troll":
                race = Troll()
            case _:
                race_selection = True
                print("Invalid input, try again")

    selected_class = ""
    character = None
    class_selection = True
    while class_selection == True:
        print("\n")
        choosen_class = input(""" Type the class you like to play:
                            1.Warrior => The Warrior is a fierce melee combatant, specializing in close-range battles.
                               With high defense and unwavering resilience, they can withstand heavy blows while dealing powerful strikes.
                               Warriors rely on brute strength and endurance rather than magic, making them formidable foes in direct combat.
                              
                            2.Thief => The Thief is a swift and deadly melee fighter, striking with unmatched speed and precision.
                               While their defenses are low, they make up for it with incredible agility and devastating attacks.
                               Masters of evasion and opportunistic strikes, Thieves excel at exploiting enemy weaknesses before vanishing into the shadows.
                              
                            3.Mage => The Mage is a master of arcane arts, wielding powerful spells to attack from a distance.
                              Fragile in close combat, they compensate with destructive magic, elemental control, and strategic spellcasting.
                              Whether hurling fireballs, freezing enemies in place, or bending reality itself, Mages dominate the battlefield with sheer magical prowess.
                            
                            Your input --> """).lower().strip()
        
        class_selection = False
        selected_class = choosen_class
        match (choosen_class):
            case "warrior":
                character = Warrior(race)
            case "thief":
                character = Thief(race)
            case "mage":
                character = Mage(race)
            case _:
                class_selection = True
                print("Invalid input, try again")
    selected_character = (selected_race + " " + selected_class).title()
        
    
    print(f"\033[34mYou selected {selected_character}\033[0m")
    return character


def get_spellbook(character):
    spellbook = {}
    methods = dir(character)
    for method in methods:
        if method.startswith("spell"):
            spell_function =  getattr(character, method)
            spell_name = getattr(spell_function, "spell_name", None)
            spell_description = getattr(spell_function,"spell_description",None)
            spellbook[spell_name] = method,spell_description
    return spellbook


#print(get_spellbook(Warrior(Troll())))

