import turtle

bob = turtle.Turtle()

def koch(t ,length, x):
    if x < 3:
        t.forward(length)
    else:
        koch(t, length, x / 3)
        t.left(60)
        koch(t, length, x / 3)
        t.left(120)
        koch(t, length, x / 3)
        t.left(60)
        koch(t, length, x / 3)


for i in range(3):
    koch(bob, 10, 3)

