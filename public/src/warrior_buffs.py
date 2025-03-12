def check_warrior_spirit_buff(champion):
    if champion.warrior_spirit_buff > 0:
        champion.attack += 50
        champion.defence += 50

def check_all_warrior_buffs(champion,enemy):
    check_warrior_spirit_buff(champion)
            
   
