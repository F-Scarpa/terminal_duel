from warrior_buffs import check_all_warrior_buffs
from thief_buffs import check_all_thief_buffs
#from mage_buffs import check_mage_buff


def check_all_buffs(champion,enemy):
    if champion.game_class == "warrior":
        check_all_warrior_buffs(champion,enemy)
    elif champion.game_class == "thief":
        check_all_thief_buffs(champion,enemy)
    #elif champion.game_class == "mage":
        #check_mage_all_buffs(champion,enemy)