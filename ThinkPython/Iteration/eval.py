import math

def eval_loop():
    x = 0
    y = 0
    while x != ("done"):
        x = (input("Enter an equation: "))
        if(x == ("done")):
            return(y)
        else:
            y = (eval(x))
            print(y)

eval_loop()