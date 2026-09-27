fin = open('words.txt')
word_list = [line.strip() for line in fin]

def children(word):
    children_list = []

    for i in range(len(word)):
        if (word[:i] + word[i + 1:]) in word_list:
            children_list.append(word[:i] + word[i + 1:])

    return children_list

def is_reducible(word):
    if word == '':
        return True
    for child in children(word):
        if is_reducible(child):
            return True
    return False

for line in word_list:
    word = line.strip()
    if is_reducible(word) == True:
        print(word)