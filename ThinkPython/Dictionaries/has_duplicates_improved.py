def duplicates_improved(nums):
    seen = {}
    for key in nums:
        if key in seen:
            return True
        else:
            seen[key] = 0
    else:
        return False

print(duplicates_improved(['a', 'b', 'c', 'a']))
print(duplicates_improved(['a', 'b', 'c']))