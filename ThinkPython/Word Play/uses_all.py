fin = open('words.txt')

def use_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    else:
        return True

##print(use_all(input("Enter a word: "), "aeiou"))

count = 0

for line in fin:
    word = line.strip()
    if use_all((word), "aeiouy") == True:
        count += 1

print(count)