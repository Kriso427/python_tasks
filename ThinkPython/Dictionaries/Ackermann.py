def ackermann(m,n):
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0:
        result = n+1
        memo[(m, n)] = result
        return result
    elif m > 0 and n == 0:
        result = ackermann(m-1,1)
        memo[(m, n)] = result
        return result
    elif m > 0 and n > 0:
        result = ackermann(m-1, ackermann(m, n-1))
        memo[(m, n)] = result
        return result

memo = {}

print(ackermann(3, 6))