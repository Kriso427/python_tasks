fin = open('words.txt')

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    else:
        return True

forbidden = input("enter forbidden letters: ")
count = 0

for line in fin:
    word = line.strip()
    if avoids(word, forbidden) == True:
        count += 1

print(count)