import turtle
import math

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

def draw_a (t):
    t.pensize(5)
    t.left(62)
    bob.fd(100)
    t.right(125)
    bob.fd(100)
    bob.left(180)
    bob.fd(50)
    bob.left(63)
    bob.fd(45)

def draw_b (t):
    t.pensize(6)
    for i in range (2):
        t.fd(25)
        arc(t, 30, 180)
        t.fd(29)
        t.right(180)
    t.left(180)

    t.left(90)
    t.fd(120)

def draw_c (t):
    t.pensize(6)
    t.left(140)
    arc(t, 70 , 265)


draw_c(bob)

turtle.mainloop()