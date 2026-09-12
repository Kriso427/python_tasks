import time


## append method
def words_list_append():
    start1 = time.time()

    fin = open('words.txt')
    words_list_append = []
    for line in fin:
        words_list_append.append(line.strip())

    end1 = time.time()
    print(end1 - start1)


## t = t + x method
def words_list():
    start2 = time.time()

    fin = open('words.txt')
    words_list = []
    for line in fin:
        words_list = words_list + [line.strip()]

    end2 = time.time()
    print(end2 - start2)


words_list()

words_list_append()