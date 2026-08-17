def recurse(n, s):
    if n == 1:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(-1, 0)