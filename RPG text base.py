import random

Strength = 0
Dexterity = 0
Constitution = 0
Intelligence = 0
Wisdom = 0
Charisma = 0

user_name = input("Welcome to the world of Arsolf, this world is full of danger, glory as well as many new ideas, but "
                  "first what is your name?")

class_set = input("What class do you wish to be in this world, a strong fighter, a crafty wizard "
                  "a thief, or a shopkeeper")

if class_set == "fighter":
    Strength = random.randrange(5, 10)
    Dexterity = random.randrange(3, 6)
    Constitution = random.randrange(5, 10)
    Intelligence = random.randrange(3, 6)
    Wisdom = random.randrange(3, 6)
    Charisma = random.randrange(3, 6)
elif class_set == "wizard":
    Strength = random.randrange(2, 5)
    Dexterity = random.randrange(3, 6)
    Constitution = random.randrange(2, 5)
    Intelligence = random.randrange(6, 10)
    Wisdom = random.randrange(5, 10)
    Charisma = random.randrange(3, 6)
elif class_set == "thief":
    Strength = random.randrange(4, 8)
    Dexterity = random.randrange(6, 10)
    Constitution = random.randrange(3, 6)
    Intelligence = random.randrange(3, 6)
    Wisdom = random.randrange(3, 6)
    Charisma = random.randrange(4, 8)
elif class_set == "shopkeeper":
    Strength = random.randrange(3, 5)
    Dexterity = random.randrange(4, 5)
    Constitution = random.randrange(3, 5)
    Intelligence = random.randrange(3, 5)
    Wisdom = random.randrange(5, 10)
    Charisma = random.randrange(5, 10)

print(Strength, Dexterity, Charisma, Constitution, Intelligence, Wisdom)
