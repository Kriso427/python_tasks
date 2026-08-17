import turtle

bob = turtle.Turtle()

def star(t, size):
    t.left(112)

    t.fillcolor("yellow")
    t.pencolor("black")
    t.pensize(2)

    t.begin_fill()
    for i in range(5):
        bob.fd(size)
        bob.lt(135)
        bob.fd(size)
        t.right(63)

    t.end_fill()


star(bob, 100)

turtle.mainloop()