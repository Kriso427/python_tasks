import turtle

bob = turtle.Turtle()

def heart(t, size):
    t.fillcolor("red")
    t.pencolor("black")
    t.pensize(2)

    t.begin_fill()
    t.left(140)
    t.forward(size)

    for i in range(200):
        t.right(1)
        t.forward(size * 0.0089)

    t.left(120)

    for x in range(200):
        t.right(1)
        t.forward(size * 0.0089)

    t.forward(size)
    t.end_fill()

heart(bob, 150)
turtle.mainloop()






