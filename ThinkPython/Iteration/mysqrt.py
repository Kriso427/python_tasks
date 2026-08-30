import math

def mysqrt(a):
    x = a
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < 1e-15:
            break
        x = y
    return y

print(f"{"a":<5} {"mysqrt(i)":<25} {"math.sqrt(i)":<25} {"diff":<25}")
print(f"{"-":<5} {"---------":<25} {"------------":<25} {"----":<25}")
for (i) in (range(1, 10)):
    print(f"{float(i):<5} {mysqrt(float(i)):<25} {math.sqrt(float(i)):<25} {abs(mysqrt(i)-math.sqrt(float(i))):<25}")
