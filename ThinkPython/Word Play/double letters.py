fin = open('words.txt')

def double_letters(word):
    for i in range(0, len(word) - 5, 1):
        if word[i] == word[i+1] and word[i+2] == word[i+3 ]and word[i+4] == word[i+5]:
            return True
    else:
        return False

for line in fin:
    word = line.strip()
    if double_letters(word) == True:
        print(word)
