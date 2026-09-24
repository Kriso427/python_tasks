from ThinkPython.Dictionaries.pronounce import read_dictionary
pron_dict = read_dictionary('C:\\Users\\krish\\python-tasks\\ThinkPython\\Dictionaries\\c06d.txt')

def homophones(word):
    if len(word) == 5:
        if word[1:] in pron_dict and word[0] + word[2:] in pron_dict and word in pron_dict:
            if (pron_dict[word[1:]]) == (pron_dict[word]) and (pron_dict[word]) == (pron_dict[word[0]+word[2:]]):
                return pron_dict[word[1:]]

##print(homophones('hello'))

fin = open('words.txt')
word_list = [line.strip() for line in fin]

for line in word_list:
    word = line.strip()
    if homophones(word):
        print (word)