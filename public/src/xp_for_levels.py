needed_xp = []
needed_xp.append(0)
max_level = 5
base_xp_needed = 5000
multiplier = 1


for i in range(max_level):
    levelxp = int(base_xp_needed * multiplier)
    multiplier *= 1.45
    needed_xp.append(levelxp)

#print(needed_xp)