def is_triangle():
    print ("can these lengths create a triangle")
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    c = int(input("Input c: "))
    if (a + b) > c :
        if (b + c) > a :
            if (c + a) > b :
                print ("yes")
    else:
        print("no")

is_triangle()