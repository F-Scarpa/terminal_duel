def orc_racial(champion,modifier):
    if champion.race == "orc" and champion.hp <= (champion.totalhp//2):
        champion.attack += modifier
    return True
    
        