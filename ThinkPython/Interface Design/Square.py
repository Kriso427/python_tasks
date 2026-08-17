import turtle

bob = turtle.Turtle()

def square(t):
    for i in range(4):
        bob.fd(100)
        bob.lt(90)

square(100)

turtle.mainloop()