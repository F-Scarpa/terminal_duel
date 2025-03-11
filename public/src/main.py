from create_character import create_character

from transition import transiction_phase
def main():
    phases = 0
    if phases == 0:
        character = create_character()
        phases = 1



    while phases == 1:
        transiction_phase(character)
    


 



if __name__ == "__main__":
    main()