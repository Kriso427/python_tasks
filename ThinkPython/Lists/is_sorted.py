def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] >= nums[i + 1]:
            return False
    else:
        return True

print(is_sorted(['b', 'a']))