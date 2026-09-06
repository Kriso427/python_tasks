fin = open('words.txt')

def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] >= word[i + 1]:
            return False
    else:
        return True

count = 0

for line in fin:
    word = line.strip()
    if is_abecedarian(word) == True:
        count += 1

print(count)
