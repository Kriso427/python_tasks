from ThinkPython.Lists.in_bisect import in_bisect

def reversed_pair():
    fin = open('words.txt')
    word_list = [line.strip() for line in fin]

    count = 0

    for line in word_list:
        word1 = line.strip()
        if in_bisect(word_list , word1[::-1]) == True:
            count += 1
    print (count)

reversed_pair()


