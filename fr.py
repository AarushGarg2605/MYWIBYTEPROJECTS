import turtle
import random

# =========================
# Screen Setup
# =========================

screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("orange")  # Sunset sky

# =========================
# Draw Sun
# =========================

sun = turtle.Turtle()
sun.hideturtle()
sun.speed(0)
sun.penup()
sun.goto(250, 150)
sun.color("gold")

sun.begin_fill()
sun.circle(60)
sun.end_fill()

# =========================
# Draw Grass
# =========================

ground = turtle.Turtle()
ground.hideturtle()
ground.speed(0)
ground.penup()
ground.goto(-500, -250)
ground.color("darkgreen")

ground.begin_fill()
for _ in range(2):
    ground.forward(1000)
    ground.right(90)
    ground.forward(300)
    ground.right(90)
ground.end_fill()

# =========================
# Main Turtle
# =========================

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# =========================
# Recursive Square Fractal
# =========================

def square(x, y, l):

    t.color("black")
    t.pensize(1)

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.goto(x + l, y)
    t.goto(x + l, y + l)
    t.goto(x, y + l)
    t.goto(x, y)

    if l > 10:
        square(x + 3/4 * l, y + 1/4 * l, l/2)
        square(x - 1/4 * l, y + 1/4 * l, l/2)


# =========================
# Fruit Tree Fractal
# =========================

def branch(sz, level):

    if level > 0:

        t.color("saddlebrown")

        if level >= 8:
            t.pensize(10)
        elif level >= 5:
            t.pensize(6)
        else:
            t.pensize(2)

        t.forward(sz)

        angle = random.randint(20, 30)

        t.right(angle)
        branch(sz * 0.75, level - 1)

        t.left(angle * 2)
        branch(sz * 0.75, level - 1)

        t.right(angle)
        t.backward(sz)

    else:
        # Leaf
        t.color("green")
        t.dot(14)

        # Fruit
        if random.random() < .99:
            t.color("red")
            t.dot(8)


# =========================
# Draw Square Fractal
# =========================

square(-100, -100, 200)

input("Press Enter to draw the sunset fruit tree...")

# =========================
# Clear only the fractal
# =========================

t.clear()

# =========================
# Draw Tree
# =========================

t.penup()
t.goto(0, -250)
t.pendown()

t.setheading(90)

branch(100, 9)

# =========================
# Finish
# =========================

turtle.done()