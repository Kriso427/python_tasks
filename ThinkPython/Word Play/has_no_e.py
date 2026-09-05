fin = open('words.txt')

def has_no_e(word):
    for letter in word:
        if letter in ("e"):
            return False
    else:
        return True

count = 0
total = 0

for line in fin:
    word = line.strip()
    total += 1
    if has_no_e(word) == True:
        count += 1

percentage = (count / total * 100)

print(f"{percentage:.2f}%")