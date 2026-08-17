def check_fermat():
    print ("^n + b^n = c^n")
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    c = int(input("Input c: "))
    n = int(input("Input n: "))

    if n > 2 and (a**n + b**n) == c**n :
        print ("holy smokes, fermat was wrong!")
    else:
        print ("No, that doesnt work")

check_fermat()