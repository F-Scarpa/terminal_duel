from colors import color_yellow
def check_debuffs(champion,enemy):
    if enemy.fireball_dot > 0:
        damage = int(champion.attack * 0.25)
        enemy.hp -= damage
        enemy.fireball_dot -= 1
        print(f"{color_yellow(f"{enemy.name} burns for {damage} damage || {enemy.fireball_dot} turns remaining")}")

    if enemy.stop_time_cc > 0:
        if enemy.hp < enemy.frozenhp:
            enemy.stop_time_cc = 0
            enemy.cc_status = "ok"
            print(color_yellow("You broke the time stop spell, enemy is no longer stuck in time"))
            return
        enemy.cc_status = "frozen in time"
        enemy.stop_time_cc -= 1
        print(f"{color_yellow(f"{enemy.name} is frozen in time for {enemy.stop_time_cc} more turns or until damaged")}")
        
    #warrior
    if enemy.deep_cut_dot > 0:
        damage = int(champion.attack * 0.5)
        enemy.hp -= damage
        enemy.deep_cut_dot -= 1
        print(f"{color_yellow(f"{enemy.name} bleeds for {damage} damage || {enemy.deep_cut_dot} turns remaining")}")
    #thief
    if enemy.shadowstep_cc > 0:
        enemy.cc_status = "stunned"
        enemy.shadowstep_cc -= 1
        print(f"{color_yellow(f"{enemy.name} is stunned for this turn")}")
        
    if enemy.paralyzed_cc > 0:
        enemy.cc_status = "stunned"
        enemy.paralyzed_cc -= 1
        print(f"{color_yellow(f"{enemy.name} is stunned for {enemy.paralyzed_cc} more turns")}")
    





"""  stun template
    if enemy.stop_time_cc > 0:
        enemy.cc_status = "frozen in time"
        enemy.stop_time_cc -= 1
        print(f"{color_yellow(f"{enemy.name} is frozen in time for {enemy.stop_time_cc} more turns or until damaged")}")
        """