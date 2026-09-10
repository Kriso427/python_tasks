def has_duplicates(nums):
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums)-1):
        if sorted_nums[i] == sorted_nums[i + 1]:
            return True
    else:
        return False

print(has_duplicates(['b', 'a', 'd', 'c', 'b']))

