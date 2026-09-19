def word_dictionary(search):
    word_d = {}
    fin = open('words.txt')
    word_list = [line.strip() for line in fin]
    for word in word_list:
        word_d[word] = 0
    if search in word_d:
        return True
    else:
        return False

print(word_dictionary('hello'))




