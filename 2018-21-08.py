import turtle
import pygame
import random
Screen = turtle.Screen()
Turtle = turtle.Turtle()
Screen.screensize(500, 500, "white")
x = 1
pygame.mixer.init()


def move():  # Forward command
    Turtle.forward(5)


def left():  # Turn left command
    Turtle.left(5)


def right():  # Turn right
    Turtle.right(5)


def back():  # Move back
    Turtle.backward(5)


def up_pen():  # Hold pen up to move over a drawn part
    Turtle.penup()


def down_pen():  # Set pen down to draw
    Turtle.pendown()


def size_up():  # Increase pen size larger
    Turtle.pensize(x+1)


def size_down():  # Set pen smaller
    Turtle.pensize(x-1)

# Change the pen color


def color_brown():
    Turtle.pencolor("brown")


def color_blue():
    Turtle.pencolor("blue")


def color_red():
    Turtle.pencolor("red")


def color_green():
    Turtle.pencolor("green")


def color_yellow():
    Turtle.pencolor("yellow")


# Draw a circle loop

def circle_input_code():
    c: turtle = Screen.numinput("Circle drawer", "Radius", 0, 10, 500)
    g = random.randrange(6, 11)
    for y in range(1, g):
        Turtle.circle(c)
        Turtle.right(45)
        c = c - 1
        if c == 0:
            break
    Screen.listen()

# Fill command


def star_fill_shape():
    Turtle.begin_fill()


def end_fill_shape():
    Turtle.end_fill()


def fill_color_red():
    Turtle.fillcolor("red")


def fill_color_blue():
    Turtle.fillcolor("blue")


def fill_color_brown():
    Turtle.fillcolor("brown")


def fill_color_yellow():
    Turtle.fillcolor("yellow")


def fill_color_green():
    Turtle.fillcolor("green")


def square_loop():
    s = Screen.numinput("size of Square", "length of square", 10, 10, 100)
    for d in range(1, 5):
        Turtle.forward(s)
        Turtle.right(90)
        Screen.listen()


Screen.listen()
Screen.update()
Screen.onkeypress(move, "Up")
Screen.onkeypress(left, "Left")
Screen.onkeypress(right, "Right")
Screen.onkeypress(back, "Down")
Screen.onkeypress(up_pen, "q")
Screen.onkeypress(down_pen, "w")
Screen.onkeypress(size_up, "=")
Screen.onkeypress(size_down, "-")
Screen.onkeypress(color_brown, "1")
Screen.onkeypress(color_blue, "2")
Screen.onkeypress(color_green, "3")
Screen.onkeypress(color_red, "4")
Screen.onkeypress(color_yellow, "5")
Screen.onkeypress(fill_color_blue, "@")
Screen.onkeypress(fill_color_brown, "!")
Screen.onkeypress(fill_color_green, "#")
Screen.onkeypress(fill_color_red, "$")
Screen.onkeypress(fill_color_yellow, "%")
Screen.onkeypress(circle_input_code, "c")
Screen.onkeypress(star_fill_shape, "z")
Screen.onkeypress(end_fill_shape, "x")
Screen.onkeypress(square_loop, "s")
Screen.mainloop()
