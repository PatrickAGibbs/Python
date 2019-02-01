import random
Player_level = 1
Strength = 0
Dexterity = 0
Constitution = 0
Intelligence = 0
Wisdom = 0
Charisma = 0
bombs = 5
cats = 5
med = 5
user_name = input("Welcome to the world of Arsolf, this world is full of danger, glory as well as many new ideas, but "
                  "first what is your name?")
race_set = input("What race would you want to be in this world, [e]lf, [h]uman, [o]rc, [d]ark elf or [f]airy ? ")
if race_set == "e":
    Strength = 3
    Dexterity = 5
    Constitution = 3
    Intelligence = 5
    Wisdom = 5
    Charisma = 5
elif race_set == "h":
    Strength = 4
    Dexterity = 4
    Constitution = 4
    Intelligence = 4
    Wisdom = 4
    Charisma = 4
elif race_set == "o":
    Strength = 5
    Dexterity = 3
    Constitution = 5
    Intelligence = 3
    Wisdom = 3
    Charisma = 2
elif race_set == "d":
    Strength = 3
    Dexterity = 5
    Constitution = 4
    Intelligence = 4
    Wisdom = 4
    Charisma = 5
elif race_set == "f":
    Strength = 3
    Dexterity = 4
    Constitution = 2
    Intelligence = 5
    Wisdom = 5
    Charisma = 5
else:
    print("so a smart one huh well, ill show you")
    Strength = 1
    Dexterity = 1
    Constitution = 1
    Intelligence = 1
    Wisdom = 1
    Charisma = 1

class_set = input("What class do you wish to be in this world, a strong [f]ighter, a crafty [w]izard "
                  "a [t]hief, or a [s]hopkeeper")

if class_set == "f":
    Strength = Strength + random.randrange(5, 10)
    Dexterity = Dexterity + random.randrange(3, 6)
    Constitution = Constitution + random.randrange(5, 10)
    Intelligence = Intelligence + random.randrange(3, 6)
    Wisdom = Wisdom + random.randrange(3, 6)
    Charisma = Charisma + random.randrange(3, 6)
elif class_set == "w":
    Strength = Strength + random.randrange(2, 5)
    Dexterity = Dexterity + random.randrange(3, 6)
    Constitution = Constitution + random.randrange(2, 5)
    Intelligence = Intelligence + random.randrange(6, 10)
    Wisdom = Wisdom + random.randrange(5, 10)
    Charisma = Charisma + random.randrange(3, 6)
elif class_set == "t":
    Strength = Strength + random.randrange(4, 8)
    Dexterity = Dexterity + random.randrange(6, 10)
    Constitution = Constitution + random.randrange(3, 6)
    Intelligence = Intelligence + random.randrange(3, 6)
    Wisdom = Wisdom + random.randrange(3, 6)
    Charisma = Charisma + random.randrange(4, 8)
elif class_set == "s":
    Strength = Strength + random.randrange(3, 5)
    Dexterity = Dexterity + random.randrange(4, 5)
    Constitution = Constitution + random.randrange(3, 5)
    Intelligence = Intelligence + random.randrange(3, 5)
    Wisdom = Wisdom + random.randrange(5, 10)
    Charisma = Charisma + random.randrange(5, 10)
else:
    print("so a smart one huh well, ill show you")
    Strength = 1
    Dexterity = 1
    Constitution = 1
    Intelligence = 1
    Wisdom = 1
    Charisma = 1
gold = Charisma * 5
print(user_name, Strength, Intelligence, Constitution, Charisma, Wisdom, Dexterity, gold)
player_hp = Constitution * Player_level
goblin_life = Player_level * 10
player_hp = Constitution * Player_level
while player_hp > 1:
    placement = input("walking down the woods you come to a fork in the road, one leads to the [t]own while the other "
                      "leads deeper into the [f]orest")
    while placement == "t":
        town_loc = input("You enter the small town of Golla and see the following spots, a [m]arket , a [t]avern and a "
                         "[r]est stop or [l]eave.")
        while town_loc == "m":
            yes_no = input("do you wish to buy any of my wares[y/n]?")
            if yes_no == "y":
                choice = input("what do you wish to buy, [b]ombs of 25g, [c]ats for 30g, [m]ed for 10g")
                if choice == "b":
                    if gold >= 25:
                        gold = gold - 25
                        bombs = 1 + bombs
                        print("you bought a bomb", bombs)
                    elif gold < 25:
                        print("sorry you cant pay")
                if choice == "c":
                    if gold >= 30:
                        gold = gold - 30
                        cats = cats + 1
                        print("you bought a cat", cats)
                    elif gold < 30:
                        print("sorry you don't have the gold for it")
                if choice == "m":
                    if gold >= 10:
                        gold = gold - 10
                        med = med + 1
                        print("you buy medicine", med)
                    elif gold < 10:
                        print("sorry you don't have the gold for that")
                if choice != "c" or "m" or "b":
                    print("sorry i don`t have that")
            if yes_no == "n":
                print("See you soon")
                break
        while town_loc == "t":
            Tavern_command = input("welcome, would you like to hear some tips from the creator.[y/n]")
            if Tavern_command == "y":
                print("never")
                break
            elif Tavern_command == "n":
                print("Ok, see you again")
                break
        while town_loc == "r":
            print("you rest for a day")
            player_hp = Constitution * Player_level
            break
        if town_loc == "l":
            print("you leave the town")
            break

    if placement == "f":
        print("A goblin attacks")
        while goblin_life >= 1:
            command_line = input("what will you do, [a]ttack, [b]ag, or [r]un?")
            if command_line == "a":
                if class_set == "f":
                    fightr_attack = input("Ok fighter, what will you  do fighter,[p]unch,[k]ick,[t]ackle")
                    if fightr_attack == "p":
                        punch_damage = Strength * Player_level / 2
                        goblin_life = goblin_life - punch_damage
                        print("you punched delt", punch_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print("goblin delt ", goblin_damage)
                    elif fightr_attack == "k":
                        kick_damage = Strength * Player_level / 2
                        goblin_life = goblin_life - kick_damage
                        chance = random.randrange(1, 100)
                        print("You delt ", kick_damage)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print("Goblin delt", goblin_damage)
                    elif fightr_attack == "t":
                        tackle_damage = Strength * Player_level / 2
                        goblin_life = goblin_life - tackle_damage
                        chance = random.randrange(1, 100)
                        print("Goblin delt", tackle_damage)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                elif class_set == "w":
                    wizard_attack = input("what will you do wizard, [fl]ames, [fr]ost, [s]hock. ")
                    if wizard_attack == "fl":
                        flame_damage = Intelligence * Player_level / 2
                        goblin_life = goblin_life - flame_damage
                        print("You delt", flame_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print("Goblin delt", goblin_damage)
                    elif wizard_attack == "fr":
                        frost_damage = Intelligence * Player_level / 2
                        goblin_life = goblin_life - frost_damage
                        chance = random.randrange(1, 100)
                        print("Frost delt", frost_damage)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print("Goblin delt", goblin_damage)
                    elif wizard_attack == "s":
                        shock_damage = Intelligence * Player_level / 2
                        goblin_life = goblin_life - shock_damage
                        print("You delt", shock_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print("Goblin delt", goblin_damage)
                elif class_set == "t":
                    thief_attack = input("what will you do thief, [s]tab, [d]ash, [t]akedown.")
                    if thief_attack == "s":
                        stab_damage = Strength * Player_level / random.randrange(1,10)
                        goblin_life = goblin_life - stab_damage
                        print("You delt", stab_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print("Goblin delt", goblin_damage)
                    elif thief_attack == "d":
                        dash_damage = Strength * Player_level / random.randrange(1,10)
                        goblin_life = goblin_life - dash_damage
                        print("You dashed for", dash_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print("Goblin delt", goblin_damage)
                    elif thief_attack == "t":
                        take_down_damage = Strength * Player_level / random.randrange(1,10)
                        goblin_life = goblin_life - take_down_damage
                        print("You delt", take_down_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            print("Goblin delt", goblin_damage)
                            player_hp = player_hp - goblin_damage
                elif class_set == "s":
                    shopkeeper_attack = input("what can you do, [s]lap, [r]am, [j]ump?")
                    if shopkeeper_attack == "s":
                        slap_damage = Strength * Player_level / random.randrange(1,10)
                        goblin_life = goblin_life - slap_damage
                        chance = random.randrange(1, 100)
                        print("You delt", slap_damage)
                    if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print("Goblin delt", goblin_damage)
                    elif shopkeeper_attack == "r":
                        ram_damage = Strength * Player_level % 2
                        goblin_life = goblin_life - ram_damage
                        chance = random.randrange(1, 100)
                        print("You delt", ram_damage)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print("Goblin delt", goblin_damage)
                    elif shopkeeper_attack == "j":
                        jump_damage = Strength * Player_level % 2
                        goblin_life = goblin_life - jump_damage
                        chance = random.randrange(1, 100)
                        print("You delt", jump_damage)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print("Goblin delt", goblin_damage)
            elif command_line == "b":
                bag_item = input("what will you use , [m]ed, [b]omb, [c]at?")
                if bag_item == "m":
                    player_hp = player_hp + Wisdom
                    chance = random.randrange(1, 100)
                    print("You healed for", Wisdom)
                    med = med - 1
                    if chance % random.randrange(1, 100) == 0:
                        goblin_damage = random.randrange(1, 5)
                        player_hp = player_hp - goblin_damage
                        print(goblin_damage)
                elif bag_item == "b":
                    if bombs >= 0:
                        goblin_life = goblin_life - 5
                        bombs = bombs - 1
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print(goblin_damage)
                elif bag_item == "c":
                    print("why are you using a cat")
                    goblin_life = goblin_life - 4
                    chance_1 = random.randrange(1, 100)
                    chance = random.randrange(1, 100)
                    cats = cats - 1
                    if chance_1 % random.randrange(1, 10) == 0:
                        print("the cat attacks again")
                        goblin_life = goblin_life - 4
                    if chance % random.randrange(1, 100) == 0:
                        player_hp = player_hp - random.randrange(1, 5)
                elif bag_item != "m" or "b" or "c":
                    print("you fumble with your bag")
                    chance = random.randrange(1, 100)
                    if chance % random.randrange(1, 100) == 0:
                        player_hp = player_hp - random.randrange(1, 5)
            elif command_line == "run":
                chance = random.randrange(0, 100)
                if chance % 2 == 0:
                    break
                else:
                    print("you fail to run")
            else:
                print("you fail to move")
                chance = random.randrange(1, 100)
                if chance % random.randrange(1, 100) == 0:
                    goblin_damage = random.randrange(1, 5)
                    player_hp = player_hp - goblin_damage
                    print(goblin_damage)
            print(player_hp, goblin_life)
        if goblin_life <= 0:
            print("the goblin falls before you")
            increase_gold = random.randrange(0,26)
            gold = gold + increase_gold
            print("the goblin drops ", increase_gold, " gold")
if player_hp == 0:
    print("you have fallen in battle")
    quit()

