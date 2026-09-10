def chop(a):
    nums = (a)
    del nums[0]
    del nums[-1]

t = [1, 2, 3, 4, 5, 6]
chop(t)
print(t)