import turtle
import time
t = time.localtime()
s = int(time.strftime("%S",t))
m = int(time.strftime("%M",t))
h = int(time.strftime("%H",t))

outline= turtle.Turtle()
outline.hideturtle()
outline.goto(0,-150)
outline.clear()
outline.fillcolor("#F5F5F5")
outline.begin_fill()
outline.circle(150)
outline.end_fill()

sec= turtle.Turtle()
sec.hideturtle()
sec.pencolor("red")
sec.pensize(2)
sec.left(90)
sec.right(s*6)

min= turtle.Turtle()
min.hideturtle()
min.pensize(1)
min.left(90)
min.right(m*6)
min.forward(100) 
min.backward(100)

hour = turtle.Turtle()
hour.hideturtle()
hour.pensize(4)
hour.left(90)
hour.right((h*30) + (m/2))
hour.forward(100) 
hour.backward(100)


def seconds():
    time.sleep(0.7)
    sec.clear()
    sec.goto(0,0)
    sec.speed(10)
    sec.forward(120)
    sec.backward(120)
    sec.right(6)

def mins():
    min.clear()
    min.right(5)
    min.forward(100) 
    min.backward(100)

for i in range(61-s):
    seconds()
mins()

while True:

    for i in range(60):
        seconds()
    mins()
hour.right(0.5)

#work herer
    



while True:
    time.sleep(1)
    break


