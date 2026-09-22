def rotate_word(word, num):
    rotated = ""
    for letter in word:
        if letter.isupper():
            rotated += chr(((ord(letter) - (ord('A')) + num) % 26) + ord('A'))
        else:
            rotated += chr(((ord(letter) - (ord('a')) + num) % 26) + ord('a'))
    return rotated

fin = open('words.txt')
word_list = [line.strip() for line in fin]

for word in word_list:
    for i in range(1, 26):
        if (rotate_word(word, i)) in word_list:
            print (rotate_word(word, i), word)

