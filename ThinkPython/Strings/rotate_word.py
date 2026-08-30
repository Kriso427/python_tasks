def rotate_word(word, num):
    rotated = ""
    for letter in word:
        if letter.isupper():
            rotated += chr(((ord(letter) - (ord('A')) + num) % 26) + ord('A'))
        else:
            rotated += chr(((ord(letter) - (ord('a')) + num) % 26) + ord('a'))
    return rotated

print(rotate_word('cubed', 10))