def check_warrior_spirit_buff(warrior,modifier):
    if warrior.game_class == "warrior":
        if warrior.warrior_spirit_buff > 0:
            warrior.attack += modifier
            warrior.defence += modifier
            
   
