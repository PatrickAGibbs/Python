import random
Player_level = 1
Strength = 0
Dexterity = 0
Constitution = 0
Intelligence = 0
Wisdom = 0
Charisma = 0
bombs = 5


def goblin_attack_command():
    player_hp = Constitution * Player_level
    goblin_life = Player_level * 10
    print("a goblin appears before you")
    bombss = bombs
    while player_hp > 1 :
        while goblin_life >= 1:
            command_line = input("what will you do, attack, bag, or run?")
            if command_line == "attack":
                if class_set == "fighter":
                    fightr_attack = input("Ok fighter, will you  do fighter,punch,kick,tackle")
                    if fightr_attack == "punch":
                        punch_damage = Strength * Player_level % random.randrange(2, 4)
                        goblin_life = goblin_life - punch_damage
                        print(punch_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print(goblin_damage)
                    elif fightr_attack == "kick":
                        kick_damage = Strength * Player_level % random.randrange(1, 5)
                        goblin_life = goblin_life - kick_damage
                        chance = random.randrange(1, 100)
                        print(kick_damage)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print(goblin_damage)
                    elif fightr_attack == "tackle":
                        tackle_damage = Strength * Player_level % random.randrange(1, 3)
                        goblin_life = goblin_life - tackle_damage
                        chance = random.randrange(1, 100)
                        print(tackle_damage)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                elif class_set == "wizard":
                    wizard_attack = input("what will you do wizard, flames, frost, shock. ")
                    if wizard_attack == "flames":
                        flame_damage = Intelligence * Player_level % random.randrange(2, 4)
                        goblin_life = goblin_life - flame_damage
                        print(flame_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print(goblin_damage)
                    elif wizard_attack == "frost":
                        frost_damage = Intelligence * Player_level % random.randrange(1, 5)
                        goblin_life = goblin_life - frost_damage
                        chance = random.randrange(1, 100)
                        print(frost_damage)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print(goblin_damage)
                    elif wizard_attack == "shock":
                        shock_damage = Intelligence * Player_level % random.randrange(1, 3)
                        goblin_life = goblin_life - shock_damage
                        print(shock_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print(goblin_damage)
                elif class_set == "thief":
                    thief_attack = input("what will you do thief, stab, dash, takedown.")
                    if thief_attack == "stab":
                        stab_damage = Strength * Player_level % random.randrange(1, 5)
                        goblin_life = goblin_life - stab_damage
                        print(stab_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print(goblin_damage)
                    elif thief_attack == "dash":
                        dash_damage = Strength * Player_level % random.randrange(1, 7)
                        goblin_life = goblin_life - dash_damage
                        print(dash_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print(goblin_damage)
                    elif thief_attack == "take down":
                        take_down_damage = Strength * Player_level % random.randrange(1, 10)
                        goblin_life = goblin_life - take_down_damage
                        print(take_down_damage)
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            print(goblin_damage)
                            player_hp = player_hp - goblin_damage
                    elif class_set == "shopkeeper":
                        shopkeeper_attack = input("what can you do, slap, ram, jump?")
                        if shopkeeper_attack == "slap":
                            slap_damage = Strength * Player_level % random.randrange(1, 5)
                            goblin_life = goblin_life - slap_damage
                            chance = random.randrange(1, 100)
                            print(slap_damage)
                            if chance % random.randrange(1, 100) == 0:
                                goblin_damage = random.randrange(1, 5)
                                player_hp = player_hp - goblin_damage
                                print(goblin_damage)
                        elif shopkeeper_attack == "ram":
                            ram_damage = Strength * Player_level % random.randrange(1, 7)
                            goblin_life = goblin_life - ram_damage
                            chance = random.randrange(1, 100)
                            print(ram_damage)
                            if chance % random.randrange(1, 100) == 0:
                                goblin_damage = random.randrange(1, 5)
                                player_hp = player_hp - goblin_damage
                                print(goblin_damage)
                        elif shopkeeper_attack == "jump" :
                            jump_damage = Strength * Player_level % random.randrange(1,10)
                            goblin_life = goblin_life - jump_damage
                            chance = random.randrange(1, 100)
                            print(jump_damage)
                            if chance % random.randrange(1, 100) == 0:
                                goblin_damage = random.randrange(1, 5)
                                player_hp = player_hp - goblin_damage
                                print(goblin_damage)
            elif command_line == "bag":
                bag_item = input("what will you use , med, bomb, cat?")
                if bag_item == "med":
                    player_hp = player_hp + Wisdom
                    chance = random.randrange(1, 100)
                    print(Wisdom)
                    if chance % random.randrange(1, 100) == 0:
                        goblin_damage = random.randrange(1, 5)
                        player_hp = player_hp - goblin_damage
                        print(goblin_damage)
                elif bag_item == "bomb":
                    if bombss >= 0:
                        goblin_life = goblin_life - 5
                        bombss = bombss - 1
                        chance = random.randrange(1, 100)
                        if chance % random.randrange(1, 100) == 0:
                            goblin_damage = random.randrange(1, 5)
                            player_hp = player_hp - goblin_damage
                            print(goblin_damage)
                elif bag_item == "cat":
                    print("why are you using a cat")
                    goblin_life = goblin_life - 4
                    chance_1 = random.randrange(1, 100)
                    chance = random.randrange(1, 100)
                    if chance_1 % random.randrange(1, 10) == 0:
                        print("the cat attacks again")
                        goblin_life = goblin_life - 4
                    if chance % random.randrange(1, 100) == 0:
                        player_hp = player_hp - random.randrange(1, 5)
                else:
                    print("you fumble with your bag")
                    chance = random.randrange(1, 100)
                    if chance % random.randrange(1, 100) == 0:
                        player_hp = player_hp - random.randrange(1, 5)
            else:
                print("you fail to move")
                chance = random.randrange(1, 100)
                if chance % random.randrange(1, 100) == 0:
                    goblin_damage = random.randrange(1, 5)
                    player_hp = player_hp - goblin_damage
                    print(goblin_damage)
            print(player_hp, goblin_life)
        print("the goblin falls before you")
        break
    if player_hp == 0:
        print("you have fallen in battle")
        quit()


user_name = input("Welcome to the world of Arsolf, this world is full of danger, glory as well as many new ideas, but "
                  "first what is your name?")
race_set = input("What race would you want to be in this world, elf, human, orc, dark elf or fairy ? ")
if race_set == "elf":
    Strength = 3
    Dexterity = 5
    Constitution = 3
    Intelligence = 5
    Wisdom = 5
    Charisma = 5
elif race_set == "human":
    Strength = 4
    Dexterity = 4
    Constitution = 4
    Intelligence = 4
    Wisdom = 4
    Charisma = 4
elif race_set == "orc":
    Strength = 5
    Dexterity = 3
    Constitution = 5
    Intelligence = 3
    Wisdom = 3
    Charisma = 2
elif race_set == "dark elf":
    Strength = 3
    Dexterity = 5
    Constitution = 4
    Intelligence = 4
    Wisdom = 4
    Charisma = 5
elif race_set == "fairy":
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

class_set = input("What class do you wish to be in this world, a strong fighter, a crafty wizard "
                  "a thief, or a shopkeeper")

if class_set == "fighter":
    Strength = Strength + random.randrange(5, 10)
    Dexterity = Dexterity + random.randrange(3, 6)
    Constitution = Constitution + random.randrange(5, 10)
    Intelligence = Intelligence + random.randrange(3, 6)
    Wisdom = Wisdom + random.randrange(3, 6)
    Charisma = Charisma + random.randrange(3, 6)
elif class_set == "wizard":
    Strength = Strength = Strength + random.randrange(2, 5)
    Dexterity = Dexterity + random.randrange(3, 6)
    Constitution = Constitution + random.randrange(2, 5)
    Intelligence = Intelligence + random.randrange(6, 10)
    Wisdom = Wisdom + random.randrange(5, 10)
    Charisma = Charisma + random.randrange(3, 6)
elif class_set == "thief":
    Strength = Strength + random.randrange(4, 8)
    Dexterity = Dexterity + random.randrange(6, 10)
    Constitution = Constitution + random.randrange(3, 6)
    Intelligence = Intelligence + random.randrange(3, 6)
    Wisdom = Wisdom + random.randrange(3, 6)
    Charisma = Charisma + random.randrange(4, 8)
elif class_set == "shopkeeper":
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
print(user_name, class_set, race_set, Strength, Intelligence, Constitution, Charisma, Wisdom, Dexterity)
goblin_attack_command()
print("end of combat")
