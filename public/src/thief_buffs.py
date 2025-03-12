def check_shadowstep_buff(champion,modifier):
    if champion.game_class == "thief":
        if champion.shadowstep_buff:
            champion.attack *= 1.4
            