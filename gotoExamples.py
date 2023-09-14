import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.penup()
t.goto(-200,200)
for i in range(30):
    t.left(10)

t.goto(200,200)
for i in range(30):
    t.left(10)

t.goto(200,-200)
for i in range(30):
    t.left(10)

t.goto(-200,-200)
for i in range(30):
    t.left(10)
