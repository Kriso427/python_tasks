def gc(a, b):
    if a >= b:
        c = b
        while c > 0:
            if a % c == 0 and b % c == 0:
                return c
            c -= 1
    elif b >= a :
        c = a
        while c > 0:
            if a % c == 0 and b % c == 0:
                return c
            c -= 1


print(gc(50, 60))
