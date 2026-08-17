import turtle
import math

bob = turtle.Turtle()

def spiral(t, start, expand, turns):
    angle_step = 5
    steps = int((360 * turns) / angle_step)

    for i in range(steps):
        angle = math.radians(i * angle_step)
        r = start + expand * angle
        t.setheading(i * angle_step)
        t.goto(r * math.cos(angle),
               r * math.sin(angle))

spiral(bob, 0, 10, 3)