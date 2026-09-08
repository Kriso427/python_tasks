def cumsum(a):
    nums = a
    total = 0
    newlist = []
    for i in nums:
        total += i
        newlist.append(total)
    return newlist

print(cumsum([1,2,3,4,5,6]))

