from warrior_buffs import check_warrior_spirit_buff
from thief_buffs import check_shadowstep_buff


def check_all_buffs(champion,enemy):
    check_warrior_spirit_buff(champion,enemy)
    check_shadowstep_buff(champion,enemy)