def use_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    else:
        return True

print(use_only(input("Enter a word: "), "acefhlo"))

