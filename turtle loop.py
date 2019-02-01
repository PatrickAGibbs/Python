import turtle

x = 0
y = 0
a = 0

b = 0
c = 0

d = 0
e = 0
f = 0
yes_no = input("Do you want to play a game?")
if yes_no != "yes" or yes_no != "no":
    print("Sorry I didn't get that")
    yes_no = input("Do you want to play a game?")
if yes_no == "yes":
    x = input("How many times do you you want me to run?")
    y = input("How many steps do you want me to move? ")
    c = input("How much should i turn left by?")
    b = input("How much should i go back.")
    a = input("how much should i turn right")
    d = input(" what R shade")
    e = input(" what b shade")
    f = input(" what green shade")
if yes_no == "no":
    print("Ok i understand")
    quit()
x = int(x)
y = int(y)
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
scr = turtle.Screen()
scr.tracer(2)
scr.colormode(255)
Max = turtle.Turtle()
Max.hideturtle()
Max.pencolor((d, f, e))
for Mick in range(1, x):
    Max.forward(y + Mick)
    Max.right(a)
    Max.left(c)
    Max.backward(b)
    Max.left(c)
    Max.forward(y)
    Max.right(a)
    Max.backward(b)
scr.mainloop()
