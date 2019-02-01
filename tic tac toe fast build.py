import random

print("welcome to tic tac toe, here is the board.")

row_1 = ["1", "2", "3"]
row_2 = ["4", "5", "6"]
row_3 = ["7", "8", "9"]
print(row_1, '\n', row_2, '\n', row_3)

while True:
    user_input = input("what point do you want on the board")
    if user_input == "1":
        if row_1[0] is not "1":
            print("sorry that's taken")
        if row_1[0] == '1':
            row_1[0] = "x"
            print(row_1, '\n', row_2, '\n', row_3)

    if user_input == "2":
        if row_1[1] is not "2":
            print("sorry that's taken")
        if row_1[1] == '2':
            row_1[1] = "x"
            print(row_1, '\n', row_2, '\n', row_3)

    if user_input == "3":
        if row_1[2] is not "3":
            print("sorry that's taken")
        if row_1[2] == '3':
            row_1[2] = "x"
            print(row_1, '\n', row_2, '\n', row_3)

    if user_input == "4":
        if row_2[0] is not "4":
            print("sorry that's taken")
        if row_2[0] == '4':
            row_2[0] = "x"
            print(row_1, '\n', row_2, '\n', row_3)
    if user_input == "5":
        if row_2[1] is not "5":
            print("sorry that's taken")
        if row_2[1] == '5':
            row_2[1] = "x"
            print(row_1, '\n', row_2, '\n', row_3)
    if user_input == "6":
        if row_2[2] is not "6":
            print("sorry that's taken")
        if row_2[2] == '6':
            row_2[2] = "x"
            print(row_1, '\n', row_2, '\n', row_3)
    if user_input == "7":
        if row_3[0] is not "7":
            print("sorry that's taken")
        if row_3[0] == '7':
            row_3[0] = "x"
            print(row_1, '\n', row_2, '\n', row_3)
    if user_input == "8":
        if row_3[1] is not "8":
            print("sorry that's taken")
        if row_3[1] == '8':
            row_3[1] = "x"
            print(row_1, '\n', row_2, '\n', row_3)
    if user_input == "9":
        if row_3[2] is not "9":
            print("sorry that's taken")
        if row_3[2] == '9':
            row_3[2] = "x"
            print(row_1, '\n', row_2, '\n', row_3)
    # win row check
    if row_1[0] == row_2[0] == row_3[0]:
        print("you win")
        quit()
    if row_1[1] == row_2[1] == row_3[1]:
        print("you win")
        quit()
    if row_1[2] == row_2[2] == row_3[2]:
        print("you win")
        quit()
    if row_1[0] == row_1[1] == row_1[2]:
        print("you win")
        quit()
    if row_2[0] == row_2[1] == row_2[2]:
        print("you win")
        quit()
    if row_3[0] == row_3[1] == row_3[2]:
        print("you win")
        quit()
    if row_1[0] == row_2[1] == row_3[2]:
        print("you win")
        quit()
    if row_1[2] == row_2[1] == row_3[0]:
        print("you win")
        quit()
    bot_move = True
    while bot_move is True:
        bot_number = random.randrange(1, 10)
        print(bot_number)
        if bot_number == 1:
            if row_1[0] == '1':
                row_1[0] = "o"
                print(row_1, '\n', row_2, '\n', row_3)
                bot_move = False
        if bot_number == 2:
            if row_1[1] == '2':
                row_1[1] = "o"
                print(row_1, '\n', row_2, '\n', row_3)
                bot_move = False
        if bot_number == 3:
            if row_1[2] == '3':
                row_1[2] = "o"
                print(row_1, '\n', row_2, '\n', row_3)
                bot_move = False
        if bot_number == 4:
            if row_2[0] == '4':
                row_2[0] = "o"
                print(row_1, '\n', row_2, '\n', row_3)
                bot_move = False
        if bot_number == 5:
            if row_2[1] == '5':
                row_2[1] = "o"
                print(row_1, '\n', row_2, '\n', row_3)
                bot_move = False
        if bot_number == 6:
            if row_2[2] == '6':
                row_2[2] = "o"
                print(row_1, '\n', row_2, '\n', row_3)
                bot_move = False
        if bot_number == 7:
            if row_3[0] == '7':
                row_3[0] = "o"
                print(row_1, '\n', row_2, '\n', row_3)
                bot_move = False
        if bot_number == 8:
            if row_3[1] == '8':
                row_3[1] = "o"
                print(row_1, '\n', row_2, '\n', row_3)
                bot_move = False
        if bot_number == 9:
            if row_3[2] == '9':
                row_3[2] = "o"
                print(row_1, '\n', row_2, '\n', row_3)
                bot_move = False
        if row_1[0] == row_2[0] == row_3[0]:
            print("you lose")
            quit()
        if row_1[1] == row_2[1] == row_3[1]:
            print("you lose")
            quit()
        if row_1[2] == row_2[2] == row_3[2]:
            print("you lose")
            quit()
        if row_1[0] == row_1[1] == row_1[2]:
            print("you lose")
            quit()
        if row_2[0] == row_2[1] == row_2[2]:
            print("you lose")
            quit()
        if row_3[0] == row_3[1] == row_3[2]:
            print("you lose")
            quit()
        if row_1[0] == row_2[1] == row_3[2]:
            print("you lose")
            quit()
        if row_1[2] == row_2[1] == row_3[0]:
            print("you lose")
            quit()