fin = open('words.txt')
word_list = [line.strip() for line in fin]
word_set = set(word_list)

def children(word):
    children_list = []

    for i in range(len(word)):
        if (word[:i] + word[i + 1:]) in word_set:
            children_list.append(word[:i] + word[i + 1:])

    return children_list

memo = {}

def is_reducible(word):
    if word in memo:
        return memo[word]
    if word == '':
        memo[word] = True
        return True
    for child in children(word):
        if is_reducible(child):
            memo[word] = True
            return True
    memo[word] = False
    return False

longest = ()

for line in word_list:
    word = line.strip()
    if is_reducible(word) == True:
        if len(word) > len(longest):
            longest = word

print(longest)