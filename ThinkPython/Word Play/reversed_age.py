for diff in range(10, 50):

    count = 0
    matches = []

    for age in range(1, 100):
        mom = age + diff

        if str(age).zfill(2)[::-1] == str(mom).zfill(2):
            matches.append(age)
            count += 1

    if len(matches) == 8:
        print (matches[5])