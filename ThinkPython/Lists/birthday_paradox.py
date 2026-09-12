from random import randint

from ThinkPython.Lists.has_duplicates import has_duplicates


def birthday_paradox():
    count = 0
    for i in range(100000):
        birthdays = []
        for x in range(23):
            birthdays.append(randint(0, 365))

        sorted_birthdays = sorted(birthdays)

        if has_duplicates(sorted_birthdays):
            count += 1

    probability = (count / 100000)
    print(probability)

birthday_paradox()