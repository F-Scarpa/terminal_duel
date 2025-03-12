def check_shadowstep_buff(champion):
    if champion.shadowstep_buff:
        champion.attack *= 1.4

def check_all_thief_buffs(champion,enemy):
    check_shadowstep_buff(champion)

            