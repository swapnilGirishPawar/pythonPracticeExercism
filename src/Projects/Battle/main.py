from http.client import PAYMENT_REQUIRED
from operator import truediv
from re import M
from secrets import choice
from subprocess import check_output
from classes.game import person, bcolors


magic = [{"name": "fire", "cost": 10, "dmg": 60},
         {"name": "thunder", "cost": 8, "dmg": 48},
         {"name": "waterSplash", "cost": 3, "dmg": 24},
         ]


player = person(hp=460, mp=65, atk=60, df=34, magic=magic)

enemy = person(hp=500, mp=65, atk=45, df=24, magic=magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "ENEMY ATTACKS !! " + bcolors.ENDC)

while (running):
    # Player can choose actions in magic and attack
    print("___________________________________________")
    player.choose_action()
    choice = input(" Player Choose the action:")
    index = int(choice) - 1
    print("Your choose action index :", index)

    # if player select Attack - enemy will only take damage.
    if index == 0:
        dmg = player.generate_damage()
        print(bcolors.OKBLUE + "\n" + "PLAYER deals " +
              str(dmg), "Points of damage " + bcolors.ENDC)
        enemy.take_damage(dmg)

    # If player select Magic  - enemy take magic-spell's damage and it will reduce player's match point(MP)
    elif index == 1:
        print("dmg")
        player.choose_magic()
        magic_choice = int(input("CHoose Magic:")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)
# if player does not have enugh match points then tell player to only attack
        current_mp = player.get_mp()
        if cost > current_mp:
            print(bcolors.FAIL + bcolors.BOLD +
                  "\nYou dont have enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals " +
              str(magic_dmg), "Points of damage " + bcolors.ENDC)

    # Enemy can select magic also - code required.
    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    print(bcolors.FAIL + "\n" + "ENEMY deals " +
          str(enemy_dmg), "Points of damage " + bcolors.ENDC)
    player.take_damage(enemy_dmg)

    # Health and Damage Dashboard
    print("___________________________________________")
    print("ENEMY's HP:", bcolors.FAIL + bcolors.BOLD +
          str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)

    print("PLAYER's HP:", bcolors.OK + bcolors.BOLD +
          str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)

    print("PLAYE's MP:" + bcolors.OKBLUE + str(player.get_mp()) +
          '/' + str(player.get_max_mp()) + bcolors.ENDC)

    # End results: -
    if enemy.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "Player WON !!!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "Enemy WON !!!" + bcolors.ENDC)
        running = False
