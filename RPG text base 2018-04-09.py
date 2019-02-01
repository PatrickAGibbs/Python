import random
Player_level = 1
Strength = 0
Dexterity = 0
Constitution = 0
Intelligence = 0
Wisdom = 0
Charisma = 0

def goblin_attack_command():
    goblin_life = Player_level * 10
    print("a goblin appears before you")
    command_line = input("what will you do, attack, bag, or run?")
    if command_line == "attack":
        if class_set == "fighter":
            fightr_attack = input("Ok fighter, will you  do fighter,")
        elif class_set == "wizard":

        elif class_set == "thief":

        elif class_set == "shopkeeper":





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

