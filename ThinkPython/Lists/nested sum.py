def nested_sum(a):
    nums = (a)
    total = 0
    for item in nums:
        for i in item:
            total += i
    return total

print(nested_sum([[1, 2], [3], [4, 5, 6]]))




