import random


class Character:
    def __init__(self, name, str, dex, con, int, wis, cha, hp, exp, mana, gold, armorstr, weaponstr, staffstr
                 ):
        self.name = name
        self.mana = mana
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.hp = hp
        self.exp = exp
        self.gold = gold
        self.armorstr = armorstr
        self.weaponstr = weaponstr
        self.staffstr = staffstr


class Fighter(Character):
    def __init__(self):
        super().__init__(name=input("what is your name?"), str=random.randrange(7, 13), dex=random.randrange(4, 9),
                         con=random.randrange(6, 13), int=random.randrange(3, 8), wis=random.randrange(3, 8),
                         cha=random.randrange(1, 11), hp=10, exp=10, mana=5, gold=50, weaponstr=0,
                         armorstr=0, staffstr=0)
    prof = "fighter"
    maxhp = 10
    level = 1
    level2 = 20
    maxmana = 5
    invotory = []
    med_l = 0
    med_2 = 0
    med_3 = 0
    floor_1 = "1a1"
    setting = "forest"
    get = "patrick"
    me = "gibbs"


class Mage(Character):
    def __init__(self):
        super().__init__(name=input("what is your name?"), str=random.randrange(1, 6), dex=random.randrange(4, 6),
                         con=random.randrange(1, 5), int=random.randrange(5, 13), wis=random.randrange(3, 13),
                         cha=random.randrange(1, 6), hp=6, exp=8, mana=10, gold=50, armorstr=0,
                         weaponstr=0, staffstr=0)
    prof = "Mage"
    maxhp = 10
    level = 1
    level2 = 20
    maxmana = 10
    invotory = []
    med_l = 0
    med_2 = 0
    med_3 = 0
    floor_1 = "1a1"
    setting = "forest"
    get = "patrick"
    me = "gibbs"


class Gunslinger(Character):
    def __init__(self):
        super().__init__(name=input("what is your name?"), str=random.randrange(5, 10), dex=random.randrange(4, 6),
                         con=random.randrange(3, 10), int=random.randrange(5, 13), wis=random.randrange(3, 13),
                         cha=random.randrange(1, 6), hp=10, exp=10, mana=20, gold=150, armorstr=0,
                         weaponstr=5, staffstr=0)
    prof = "Gunslinger"
    maxhp = 10
    level = 1
    level2 = 20
    maxmana = 10
    invotory = ['pea shooter']
    med_2 = 0
    med_3 = 0
    R_ammo = 10
    S_ammo = 10
    F_ammo = 10
    M_ammo = 100
    floor_1 = "1a1"
    setting = "forest"
    get = "patrick"
    me = "gibbs"


class Goblin(Character):
    def __init__(self):
        super().__init__(name="Goblin", str=random.randrange(1, 4), dex=random.randrange(1, 4),
                         con=random.randrange(1, 4), int=random.randrange(1, 4), wis=random.randrange(1, 4),
                         cha=random.randrange(1, 4), hp=7, exp=10, mana=0, gold=random.randrange(5, 20),
                         armorstr=0, weaponstr=0, staffstr=0)
    maxmana = 0


class Orc(Character):
    def __init__(self):
        super().__init__(name="Orc", str=random.randrange(2, 5), dex=random.randrange(2, 5),
                         con=random.randrange(2, 5), int=random.randrange(2, 5), wis=random.randrange(2, 5),
                         cha=random.randrange(2, 5), hp=random.randrange(10, 20), exp=random.randrange(10, 30),
                         mana=0, gold=20, weaponstr=0, armorstr=0, staffstr=0)
    maxmana = 0


class Dragon(Character):
    def __init__(self):
        super().__init__(name="Dragon", str=random.randrange(5, 10), dex=random.randrange(5, 10),
                         con=random.randrange(5, 10), int=random.randrange(5, 10), wis=random.randrange(5, 10),
                         cha=random.randrange(2, 5), hp=random.randrange(10, 50), exp=100, mana=0, gold=100, weaponstr=0
                         , armorstr=0, staffstr=0)
    maxmana = 0


class Vampire(Character):
    def __init__(self):
        super().__init__(name="Vampire", str=random.randrange(10, 15), dex=random.randrange(5, 10),
                         con=random.randrange(5, 10), int=random.randrange(5, 10), wis=random.randrange(5, 10),
                         cha=random.randrange(2, 5), hp=random.randrange(30, 50), exp=300, mana=0, gold=500, weaponstr=5
                         , armorstr=5, staffstr=5)
    maxmana = 0


def levelUp():

    while player.exp >= player.level2:
        levelGain = True
        player.level+=1
        player.level2=player.level2*2
        gain = random.randrange(1, 10)
        if levelGain == True:
            player.maxhp += gain
            player.hp=player.maxhp
            player.maxmana += player.wis / 2
            player.mana = player.maxmana
            player.str += 5
            player.wis += 5
            player.int += 5
            player.dex += 5
            player.con += 5
            player.cha += 5
            print("You Gained a level","\n",'hp:',player.hp,"\n",'level:',player.level)
            levelGain=False


def profession():
    print("What is your class?", '\n',
          " press f for Fighter", '\n',
          " press m for Mage", '\n',
          "press g for Gunslinger")
    pclass = input(">>>")
    if pclass == "f":
        prof = Fighter()
    elif pclass == "m":
        prof = Mage()
    elif pclass == "g":
        prof = Gunslinger()
    else:
        prof = Fighter()
        # profession()
    return prof


def ranmob():
    roll = random.randrange(1, 5)
    if roll >= 2:
        mob = Goblin()
    else:
        mob = Orc()
    return mob


def maze_mob():
    roll = random.randrange(1, 10)
    if roll == 1:
        monster = Vampire()
    else:
        monster = Dragon()
    return monster


def playerAttack():
    roll = random.randrange(1, 21)
    if mob.dex < player.dex + roll:
        print("you hit")
        if player.prof == "fighter":
            dam = (player.str + player.weaponstr) * .5

        if player.prof == "Mage":
            dam = 0
            basic_comand = input("what will you do mage,A for basic attack, or S for spell or R for rest")
            if basic_comand == "A":
                dam = (player.str + player.staffstr) * .5
            if basic_comand == "S":
                spell_type = input("What spell will you do,I for ice spike for 4 mana, F for fire ball for 5 mana,"
                                   " or W for water dragon for 10.")
                if spell_type == "I":
                    if player.mana >= 4:
                        dam = player.int + player.staffstr
                        player.mana -= 4
                        print("You have", player.mana, "mana")
                    else:
                        print("you dont have enough mana")
                if spell_type == "F":
                    if player.mana >= 5:
                        dam = player.int + player.staffstr * random.randrange(1, 3)
                        player.mana -= 5
                        print("You have", player.mana, "mana")
                    else:
                        print("you dont have enough mana")
                if spell_type == "W":
                    if player.mana >= 10:
                        dam = player.int + player.staffstr * 5
                        player.mana -= 10
                        print("you have ", player.mana, "mana")
                    else:
                        print("you dont have enough mana")
            if basic_comand == "R":
                if player.mana < player.maxmana:
                    rest = player.wis
                    player.mana += rest
                    if player.mana > player.maxmana:
                        player.mana = player.maxmana
                    print("you rest for", rest, "mana, you have", player.mana, "mana")
                if player.mana >= player.maxmana:
                    print("you cannot rest")
                dam = 0
        if player.prof == "Gunslinger":
            print("you have", player.R_ammo, "normal bullets", player.S_ammo, "shock bullets", player.M_ammo,
                  "mini bullets")
            shot_choice = input("what typ of shot will you do, [n] normal, [b] burst, [u] unload.")
            if shot_choice == 'n':
                bullet_choice = input("what bullet will you do, [r] regular bullets, [s] shock bullet, [m] mini")
                if bullet_choice == 'r':
                    if player.R_ammo > 0:
                        dam = player.weaponstr
                        player.R_ammo -= 1
                if bullet_choice == 's':
                    if player.S_ammo > 0:
                        dam = player.weaponstr * 2
                        player.S_ammo -= 1
                if bullet_choice == 'm':
                    if player.M_ammo > 0:
                        dam = player.weaponstr * .5
                        player.M_ammo -= 1
                if bullet_choice == 'f':
                    if player.F_ammo > 0:
                        dam = player.weaponstr + 90
                        player.F_ammo -= 1
            if shot_choice == 'b':
                bullet_choice = input("what bullet will you do, [r] regular bullets, [s] shock bullet, [m] mini")
                if bullet_choice == 'r':
                    if player.R_ammo >= 3:
                        dam = player.weaponstr * 3
                        player.R_ammo -= 3
                if bullet_choice == 's':
                    if player.S_ammo >= 3:
                        dam = player.weaponstr * 6
                        player.S_ammo -= 3
                if bullet_choice == 'm':
                    if player.M_ammo >= 3:
                        dam = player.weaponstr * 1.5
                        player.M_ammo -= 3
                if bullet_choice == 'f':
                    if player.F_ammo >= 3:
                        dam = player.weaponstr + 180
                        player.F_ammo -= 3
            if shot_choice == 'u':
                bullet_choice = input("what bullet will you do, [r] regular bullets, [s] shock bullet, [m] mini")
                if bullet_choice == 'r':
                    dam = player.weaponstr * player.R_ammo
                    player.R_ammo -= player.R_ammo
                if bullet_choice == 's':
                    dam = player.weaponstr * 2 * player.S_ammo
                    player.S_ammo -= player.S_ammo
                if bullet_choice == 'm':
                    if player.M_ammo > 0:
                        dam = player.weaponstr * .5 * player.M_ammo
                        player.M_ammo -= player.M_ammo
                if bullet_choice == 'f':
                    dam = player.weaponstr * (player.F_ammo + 90)
                    player.F_ammo -= player.F_ammo
        mob.hp -= dam
        print("the", mob.name, "has", mob.hp, "hp left")
    else:
        print("miss")


def monsterAttack():
    dam = 0
    roll = random.randrange(1, 9)
    if roll > mob.dex-player.dex:
        print(mob.name, "deals")
        if mob.name == "Goblin":
            dam = mob.str - player.armorstr
        elif mob.name == "Orc":
            dam = mob.str - player.armorstr
        elif mob.name == "Dragon":
            dam = mob.str - player.armorstr
        if dam < 0:
            dam = 0
        print(dam, "damage")
        player.hp -= dam
        print(dam, "to you, you have", player.hp, "remaining")
    else:
        print("Monster miss")


def commands():
    if player.prof == "fighter":
        print(" press [f] to fight", '\n',
              "press [enter] to pass, or [b] for bag")
        command = input("~~~~~~~~~Press a key to Continue.~~~~~~~")
        if command == "f":
            playerAttack()
        if command == "":
            pass
        if command == 'b':
            bag()
    if player.prof == "Mage":
        print(" press [f] to fight", '\n',
              "press [enter] to pass, or [b] for bag ")
        command = input("~~~~~~~~~Press a key to Continue.~~~~~~~")
        if command == "f":
            playerAttack()
        if command == "":
            pass
        if command == 'b':
            bag()
    if player.prof == "Gunslinger":
        print(" press [f] to fight", '\n',
              "press [enter] to pass, or [b] for bag ")
        command = input("~~~~~~~~~Press a key to Continue.~~~~~~~")
        if command == "f":
            playerAttack()
        if command == "":
            pass
        if command == 'b':
            bag()


def menu():
    meun = input("[s] states, [i] inventory, [h] help")
    if meun == "s":
        print(player.name, '\n',
              "hp", player.hp, '\n',
              "manna", player.mana, '\n',
              "strength", player.str, '\n',
              "int", player.int, '\n',
              "wisdom", player.wis, '\n',
              "dexterity", player.dex, '\n',
              "constitution", player.con, '\n',
              "charisma", player.cha, '\n',
              "player ex", player.exp, '\n',
              "player level", player.level, '\n',
              "player gold", player.gold, '\n',
              "armor strength", player.armorstr, '\n',
              "weapon strength", player.weaponstr, '\n',
              "staff strength", player.staffstr, '\n',
              player.get, player.me)
    if meun == "i":
        print(player.invotory)
    if meun == "h":
        print("go to town to get armor, this is needed mainly for dragons")
        print('')
    if meun == "sea":
        player.setting = "sea"



def bag():
    if player.med_l > 0:
        print("you have", player.med_l, "basic med")
    if player.med_2 > 0:
        print("you have", player.med_2, "medium med")
    if player.med_3 > 0:
        print("you have", player.med_3, "max med")
    med_choice = input("will you use, [b] basic, [m] medium, [x] max.")
    if med_choice == "b":
        if player.med_l == 0:
            print("sorry you don't have that")
        if player.med_l > 0:
            player.hp += 5
            if player.hp > player.maxhp:
                player.hp = player.maxhp
            print("you heal for 5")
            player.med_l -= 1
    if med_choice == 'm':
        if player.med_2 == 0:
            print("sorry you don't have that")
        if player.med_2 > 0:
            player.hp += 10
            if player.hp > player.maxhp:
                player.hp = player.maxhp
            print("you heal for 10")
    if med_choice == 'x':
        if player.med_3 == 0:
            print("sorry you dont have that")
        if player.med_3 > 0:
            player.hp = player.maxhp
            print("you heal", player.maxhp - player.hp)


setting_counter = 0
mob = ranmob()
player = profession()
while True:
    while player.setting is "forest":
        life = True
        placement = input(
            "walking down the woods you come to a fork in the road, one leads to the [t]own while the other "
            "leads deeper into the [f]orest, [m] for menu")
        if placement == "m":
            menu()
        while placement == "t":
            setting_counter = 0
            town_loc = input(
                "You enter the small town of Golla and see the following spots, a [m]arket , a [t]avern and a "
                "[r]est stop or [l]eave.")
            while town_loc == "m":
                sold = input("what would you like to buy,[w] weapons, [a] armor or"
                             "[m] med or [b] bullets ")
                if sold == 'w':
                    weapon_type = input("do you want [s] swords or [a] staffs.")
                    if weapon_type == 's':
                        sword_buy = input("Do you wish to buy a [b] bronze sword for 10g or [s] silver sword for 50g")
                        if sword_buy == 'b':
                            if player.gold < 20:
                                print("you don't have the money for it")
                            if player.gold >= 20:
                                player.gold -= 20
                                print("you have bought a bronze sword")
                                player.invotory.append('bronze sword')
                                if 'bronze sword' in player.invotory:
                                    player.weaponstr += 5
                        if sword_buy == 's':
                            if player.gold < 50:
                                print("you don't have the money for it")
                            if player.gold >= 50:
                                player.gold -= 50
                                print("you have bought a silver sword")
                                player.invotory.append('silver sword')
                                if 'silver sword' in player.invotory:
                                    player.weaponstr += 10
                    if weapon_type == 'a':
                        staff_buy = input("what do you want to buy, [w] wooden staff for 20g or [g] glass staff for 50")
                        if staff_buy == 'g':
                            if player.gold < 50:
                                print("sorry you don't have enough")
                            if player.gold >= 50:
                                player.gold -= 50
                                print("you bought a glass staff")
                                player.invotory.append('glass staff')
                                if 'glass staff' in player.invotory:
                                    player.staffstr += 5
                        if staff_buy == 'w':
                            if player.gold < 20:
                                print("sorry you don't have enough")
                            if player.gold >= 20:
                                player.gold -= 20
                                print("you bought a wooden staff")
                                player.invotory.append('wooden staff')
                                if 'wooden staff' in player.invotory:
                                    player.staffstr += 2
                if sold == 'a':
                    armor_buy = input("what do you want, [r] rags 10g or [i] iron armor for 50g")
                    if armor_buy == 'r':
                        if player.gold < 10:
                            print("sorry you can`t afford that")
                        if player.gold >= 10:
                            player.gold -= 10
                            print("you have bought rags")
                            player.invotory.append('rages')
                            if 'rages' in player.invotory:
                                player.armorstr += 2
                    if armor_buy == 'i':
                        if player.gold < 50:
                            print("sorry you can`t afford that")
                        if player.gold >= 50:
                            player.gold -= 50
                            print("you have bought iron armor")
                            player.invotory.append('iron armor')
                            if 'iron armor' in player.invotory:
                                player.armorstr += 5
                if sold == 'm':
                    med_sold = input("which do you wish to buy,[l] low med ,[b] basic med ,[h] high med")
                    if med_sold == 'l':
                        player.med_l += 1
                    if med_sold == 'b':
                        player.med_2 += 1
                    if med_sold == 'h':
                        player.med_3 += 1
                if sold == "b":
                    bullet_type = input("what will you buy [r] regular 10 for 10, [s] shock 10 for 50 , or "
                                        "[m] mini 100 for 10")
                    if bullet_type == 'r':
                        if player.gold < 10:
                            print('sorry you dont have enough')
                        if player.gold >= 10:
                            player.gold -= 10
                            player.R_ammo += 10
                    if bullet_type == 's':
                        if player.gold < 50:
                            print("sorry you dont have enough")
                        if player.gold >= 50:
                            player.gold -= 50
                            player.S_ammo += 10
                    if bullet_type == 'm':
                        if player.gold < 10:
                            print("sorry you dont have enough")
                        if player.gold >= 10:
                            player.gold -= 10
                            player.M_ammo += 100
                break
            while town_loc == "t":
                Tavern_command = input("welcome, would you like to hear some tips from the creator.[y/n]")
                if Tavern_command == "y":
                    print("Go get some clothing!!")
                    break
                elif Tavern_command == "n":
                    print("Ok, see you again")
                    break
            while town_loc == "r":
                print("you rest for a day")
                player.hp = player.maxhp
                player.mana = player.maxmana
                break
            if town_loc == "l":
                print("you leave the town")
                break
        if placement == "f":
            while life == True :
                if mob.hp <= 0:
                    print('The', mob.name, 'is dead!')
                    player.exp += mob.exp
                    print('hero xp', player.exp)
                    player.gold += mob.gold
                    print(mob.name, "dropped", mob.gold, 'gold, you have', player.gold, "gold")
                    item_drop = random.randrange(1, 11)
                    if player.prof == "Gunslinger":
                        if item_drop >= 4:
                            player.M_ammo += 10
                            player.S_ammo += 10
                            player.R_ammo += 10
                    if item_drop == 2:
                        if 'gold ring of power' in player.invotory:
                            x = 0
                        if 'gold ring of power' not in player.invotory:
                            print("the monster droped the rare item")
                            player.invotory.append('gold ring of power')
                            if 'gold ring of power' in player.invotory:
                                player.weaponstr += 10
                                player.staffstr += 10
                                player.armorstr += 10

                    mob = ranmob()
                    levelUp()
                    setting_counter += 1
                    if setting_counter == 10:
                        player.setting = "sea"
                    break
                if player.hp <= 0:
                    mob.exp += player.exp
                    print("mob xp:", mob.exp)
                    print(player.name, 'died!')
                    quit()

                print("You see", mob.name + ",", mob.name, "has", mob.hp, "hp.")
                if player.hp > 0:
                    commands()
                if mob.hp > 0:
                    monsterAttack()

    while player.setting is "sea":
        print("you come to a long coast line")
        ocean_choice = input("will you enter the [t] town, [d] the dungeon")
        while ocean_choice == "t":
            town_loc = input(
                "You enter the port city of Raw and see the following spots, a [m]arket , a [t]avern and a "
                "[r]est stop or [l]eave.")
            while town_loc == "m":
                sold = input("what would you like to buy,[w] weapons, [a] armor or"
                             "[m] med. ")
                if sold == 'w':
                    weapon_type = input("do you want [s] swords or [a] staffs.")
                    if weapon_type == 's':
                        sword_buy = input("Do you wish to buy a [b] bronze sword for 10g or [s] silver sword for 50g")
                        if sword_buy == 'b':
                            if player.gold < 20:
                                print("you don't have the money for it")
                            if player.gold >= 20:
                                player.gold -= 20
                                print("you have bought a bronze sword")
                                player.invotory.append('bronze sword')
                        if sword_buy == 's':
                            if player.gold < 50:
                                print("you don't have the money for it")
                            if player.gold >= 50:
                                player.gold -= 50
                                print("you have bought a silver sword")
                                player.invotory.append('silver sword')
                    if weapon_type == 'a':
                        staff_buy = input("what do you want to buy, [w] wooden staff for 20g or [g] glass staff for 50")
                        if staff_buy == 'g':
                            if player.gold < 50:
                                print("sorry you don't have enough")
                            if player.gold >= 50:
                                player.gold -= 50
                                print("you bought a glass staff")
                                player.invotory.append('glass staff')
                        if staff_buy == 'w':
                            if player.gold < 20:
                                print("sorry you don't have enough")
                            if player.gold >= 20:
                                player.gold -= 20
                                print("you bought a wooden staff")
                                player.invotory.append('wooden staff')
                                if 'wooden staff' in player.invotory:
                                    player.staffstr += 5
                if sold == 'a':
                    armor_buy = input("what do you want, [s] silver armor 100g or [i] iron armor for 50g")
                    if armor_buy == 's':
                        if player.gold < 100:
                            print("sorry you can`t afford that")
                        if player.gold >= 100:
                            player.gold -= 100
                            print("you have bought silver")
                            player.invotory.append('silver')
                            if 'silver' in player.invotory:
                                player.armorstr += 15
                    if armor_buy == 'i':
                        if player.gold < 50:
                            print("sorry you can`t afford that")
                        if player.gold >= 50:
                            player.gold -= 50
                            print("you have bought iron armor")
                            player.invotory.append('iron armor')
                            if 'iron armor' in player.invotory:
                                player.armorstr += 10
                if sold == 'm':
                    med_sold = input("which do you wish to buy,[l] low med ,[b] basic med ,[h] high med")
                    if med_sold == 'l':
                        player.med_l += 1
                    if med_sold == 'b':
                        player.med_2 += 1
                    if med_sold == 'h':
                        player.med_3 += 1
                break
            break
        while ocean_choice == 'd':
            mob = ranmob()
            roll = random.randrange(1, 11)
            battle = False
            if roll <= 3:
                battle = True
            while battle is True:
                if mob.hp <= 0:
                    print('The', mob.name, 'is dead!')
                    player.exp += mob.exp
                    print('hero xp', player.exp)
                    player.gold += mob.gold
                    print(mob.name, "dropped", mob.gold, 'gold, you have', player.gold, "gold")
                    item_drop = random.randrange(1, 11)
                    if player.prof == "Gunslinger":
                        if item_drop >= 4:
                            player.M_ammo += 10
                            player.S_ammo += 10
                            player.R_ammo += 10
                    if item_drop == 2:
                        if 'gold ring of power' in player.invotory:
                            x = 0
                        if 'gold ring of power' not in player.invotory:
                            print("the monster droped the rare item")
                            player.invotory.append('gold ring of power')
                            if 'gold ring of power' in player.invotory:
                                player.weaponstr += 10
                                player.staffstr += 10
                                player.armorstr += 10

                    mob = ranmob()
                    levelUp()
                    setting_counter += 1
                    battle = False

                    if setting_counter == 10:
                        player.setting = "sea"

                if player.hp <= 0:
                    mob.exp += player.exp
                    print("mob xp:", mob.exp)
                    print(player.name, 'died!')
                    quit()
                print("You see", mob.name + ",", mob.name, "has", mob.hp, "hp.")
                if player.hp > 0:
                    commands()
                if mob.hp > 0:
                    monsterAttack()
            if player.floor_1 == "1a1":
                choice = input("will you go[f] 1b1, [l] 1a2 or [b] exit.")
                if choice == 'f':
                    player.floor_1 = '1b1'
                if choice == 'l':
                    player.floor_1 = '1a2'
                if choice == 'b':
                    break
            if player.floor_1 == "1b1":
                choice = input("will you go[f] 1c1 or [b] 1a1.")
                if choice == 'f':
                    player.floor_1 = '1c1'
                if choice == 'b':
                    player.floor_1 = '1a1'
            if player.floor_1 == '1c1':
                choice = input("will you go[l] 1c2 or [b] 1b1.")
                if choice == 'l':
                    player.floor_1 = '1c2'
                if choice == 'b':
                    player.floor_1 = '1b1'
            if player.floor_1 == "1c2":
                choice = input("will you go [l] 1b2, [r] 1d2 or [b] 1c1. ")
                if choice == 'l':
                    player.floor_1 = '1b2'
                if choice == 'r':
                    player.floor_1 = '1d2'
                if choice == 'b':
                    player.floor_1 = '1c1'
            if player.floor_1 == "1b2":
                choice = input("will you go [r] 1b3 or [b] 1c2.")
                if choice == 'r':
                    player.floor_1 = '1b3'
                if choice == 'b':
                    player.floor_1 = "1c2"
            if player.floor_1 == '1b3':
                choice = input("what will you do, [l] 1a3, [r] 1c3 , [f] 1b4 or [b] 1b2. ")
                if choice == 'l':
                    player.floor_1 = '1a3'
                if choice == 'r':
                    player.floor_1 = '1c3'
                if choice == 'f':
                    player.floor_1 = '1b4'
                if choice == 'b':
                    player.floor_1 = '1b2'
            if player.floor_1 == '1c3':
                mob = maze_mob()
                battle = True
                while battle == True:
                    if mob.hp <= 0:
                        print('The', mob.name, 'is dead!')
                        player.exp += mob.exp
                        print('hero xp', player.exp)
                        player.gold += mob.gold
                        print(mob.name, "dropped", mob.gold, 'gold, you have', player.gold, "gold")
                        item_drop = random.randrange(1, 11)
                        if player.prof == "Gunslinger":
                            if item_drop >= 4:
                                player.M_ammo += 10
                                player.S_ammo += 10
                                player.R_ammo += 10
                        if item_drop == 2:
                            if 'gold ring of power' in player.invotory:
                                x = 0
                            if 'gold ring of power' not in player.invotory:
                                print("the monster droped the rare item")
                                player.invotory.append('gold ring of power')
                                if 'gold ring of power' in player.invotory:
                                    player.weaponstr += 10
                                    player.staffstr += 10
                                    player.armorstr += 10

                        mob = ranmob()
                        levelUp()
                        setting_counter += 1
                        battle = False

                        if setting_counter == 10:
                            player.setting = "sea"

                    if player.hp <= 0:
                        mob.exp += player.exp
                        print("mob xp:", mob.exp)
                        print(player.name, 'died!')
                        quit()
                    print("You see", mob.name + ",", mob.name, "has", mob.hp, "hp.")
                    if player.hp > 0:
                        commands()
                    if mob.hp > 0:
                        monsterAttack()
                choice = input("will you push on [f] 1d3 or go back [b] 1b3")
                if choice == 'f':
                    player.floor_1 = '1d3'
                if choice == 'b':
                    player.floor_1 = '1b3'
            if player.floor_1 == '1d3':
                print("you enter a small room and see a large chest in it")
                if player.prof == "fighter":
                    item = "Black mask"
                    player.invotory.append('Black mask')
                    if 'Black mask' in player.invotory:
                        player.weaponstr += 20
                if player.prof == "Mage":
                    item = 'Gold mask'
                    player.invotory.append('Gold mask')
                    if 'Gold mask' in player.invotory:
                        player.staffstr += 20
                if player.prof == "Gunslinger":
                    item = "hunting rifle"
                    player.invotory.append('Hunting rifle')
                    if 'Hunting rifle' in player.invotory:
                        player.weaponstr += 20
                print('you leave the room')
                player.floor_1 = '1c3'
            if player.floor_1 == '1a2':
                choice = input("will you go [f] forward 1a3, or [b] back 1a1")
                if choice == 'f':
                    player.floor_1 = '1a3'
                if choice == 'b':
                    player.floor_1 = '1a1'
            if player.floor_1 == '1a3':
                choice = input('will you go [f]forward 1a4, [l] left 1b3, [b] back 1a2')
                if choice == 'f':
                    player.floor_1 = '1a4'
                if choice == 'l':
                    player.floor_1 = '1b3'
                if choice == 'b':
                    player.floor_1 = '1a2'
            if player.floor_1 == '1a4':
                choice = input('will you go [f] forward 1a5 or [b] back 1a3')
                if choice == 'f':
                    player.floor_1 = '1a5'
                if choice == 'b':
                    player.floor_1 = '1a3'
            if player.floor_1 == '1a5':
                choice = input('dead end,[b] back 1a4')
                if choice == 'b':
                    player.floor_1 = '1a4'



































