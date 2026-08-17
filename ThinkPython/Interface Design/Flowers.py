import turtle
import math

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    arc(t, r, angle)
    t.lt(180 - angle)
    arc(t, r, angle)

def flower(t, petals, r, angle):
    for i in range(petals):
        petal(t, r, angle)
        t.lt(360 / petals)

bob.penup()
bob.setpos(-400, 0)
bob.pendown()

flower(bob, 6, 100, 60)

bob.penup()
bob.setpos(0, 0)
bob.pendown()

flower(bob, 8, 100, 90)

bob.penup()
bob.setpos(400, 0)
bob.pendown()

flower(bob, 11, 100, 49)

turtle.mainloop()







