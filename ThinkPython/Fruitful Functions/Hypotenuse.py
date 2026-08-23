def hypotenuse ():
    a = (int(input("enter first side of triangle")))
    b = (int(input("enter second side of triangle")))
    c = (a**2 + b**2)**0.5
    print(c)
    return c

hypotenuse() 