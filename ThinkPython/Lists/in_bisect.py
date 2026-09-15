def in_bisect(a, b):

    low = 0
    high = len(a)-1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] < b:
            low = mid + 1
        elif a[mid] > b:
            high = mid - 1
        elif a[mid] == b:
            return True
    return False
