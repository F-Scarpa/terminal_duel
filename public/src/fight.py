from game_classes import *
from races import *
from enemies import select_enemy,final_boss
from create_character import get_spellbook
from debuff_tracker import check_debuffs
from cd_tracker import cd_tracker,create_spell_names_list,cd_printer
from start_turn_e import start_turn_events
from won_fight import won_fight
from orc_racial import orc_racial
from colors import color_red
from warrior_buffs import check_warrior_spirit_buff
from enemy_got_damaged import enemy_got_damaged_events
from check_modifier_buffs import check_all_buffs


import sys
import time
import inspect

def reset_stats(champion):
    champion.attack = champion.dummy_attack
    champion.defence = champion.dummy_defence


__names_list = []

def fight(champion,boss = None):
    spellbook = get_spellbook(champion)
    create_spell_names_list(champion)
    if boss is None:
        enemy = select_enemy()
    else:
        enemy = final_boss
    turn_counter = 0
    choosen_spell = ""
    
    player_turn = True

    
    
    while champion.hp > 0 and enemy.hp > 0:
        reset_stats(champion)
        start_turn_enemy_hp = enemy.hp
        res = ""
        cd_printer(champion)
        
        print("=======================")
        counter = 1
        if turn_counter % 2 == 0 and player_turn == True:
            print(color_cyan("You can CTRL + c to exit game"))
            
            print("Choose an action:")
            for spell in spellbook:
                if spell is None:
                    continue
                print(f"{counter}. {spell} --> {spellbook[spell][1]}")
                counter += 1
            print("\n")
            choosen_spell = input("""Type the action you wanna take from above --> """).title().strip()
            
            print("\n")
            if choosen_spell in spellbook:
                spell_method_name = spellbook[choosen_spell][0]
                #print(spell_method_name)
                if spell_method_name.endswith("_cd"):
                    get_attr_name = spell_method_name[6:].replace("_cd","_duration")
                    cd_remaining = getattr(champion,get_attr_name)
                    if cd_remaining > 0:
                        print(f"\033[91mThe spell you typed is still on cooldown for {cd_remaining} more turns.\033[0m")
                        continue
                spell_method = getattr(champion, spell_method_name,None)
                params_num = len(inspect.signature(spell_method).parameters)
                
                orc_r = orc_racial(champion,30)
                orc_racial(champion,30)
                # warrior buff init

                #check all buffs / check_modifier_buffs.py folder
                check_all_buffs(champion,enemy)


                #print(champion.attack)

                if params_num == 1:
                    res = spell_method(enemy)
                elif params_num == 2:
                    res = champion.spell_inventory(champion,enemy)
                elif params_num == 3:
                    res = spell_method(champion,enemy,None)
                else:

                    spell_method()
                    print(enemy.hp)
                    print(start_turn_enemy_hp)
                # check if enemy got damaged, usefull for on-hit effect
                if  enemy.hp < start_turn_enemy_hp:
                    enemy_got_damaged_events(champion,enemy)


                player_turn = False
                turn_counter += 1
                if res == "back_try" or res == "no mana" or res == "no energy" or res == "no cp":
                    player_turn = True
                    turn_counter -= 1
                    orc_racial(champion,-30)
                    
            else:
                print(color_red("Typed spell was unknown"))
                player_turn = True
 
        time.sleep(.5)
        print("=======================")

        if enemy.hp <= 0:
            if boss:
                print(color_green("😊   GG! You defeated the final boss, you won the game!!!  😊"))
                sys.exit()
            else:
                #orc racial
                if orc_r == True:
                    orc_racial(champion,-30)

                won_fight(champion,enemy)
                break
            
            
        if turn_counter % 2 == 1 and player_turn == False:
            
            cd_tracker(champion)
            check_debuffs(champion,enemy)
            
            # if enemy dies by DoT
            if enemy.hp <= 0:
                if boss:
                    print(color_green("😊   GG! You defeated the final boss, you won the game!!!  😊"))
                    sys.exit()
                else:
                    # orc racial
                    if orc_r == True:
                        orc_racial(champion,-30)

                    won_fight(champion,enemy)
                    
                break

            enemy.attack(champion)



            start_turn_events(champion,enemy)
            if enemy.hp <= 0:
                if boss:
                    print(color_green("😊   GG! You defeated the final boss, you won the game!!!  😊"))
                    sys.exit()
                else:
                    # orc racial
                    if orc_r == True:
                        orc_racial(champion,-30)

                    won_fight(champion,enemy)
                    
                break

            
            turn_counter += 1
            player_turn = True

            
            if orc_r == True:
                orc_racial(champion,-30)
            
            
            time.sleep(.5)
            
            
            
            
        if champion.hp <= 0:
            if champion.is_defeated(champion) == True:
                break
        print("=======================")


#champion = Thief(Orc())
#fight(champion)
