from ThinkPython.Lists.in_bisect import in_bisect

##checks whether a word has 2 interlocking words within it
def interlock(word):
    even = word[::2]
    odd = word[1::2]
    fin = open('words.txt')
    word_list = [line.strip() for line in fin]
    if in_bisect(word_list, even) and in_bisect(word_list, odd):
        print (word[::2], word[1::2])

##interlock("schooled")



##all possible words with a combination of 3 interlocking words
def interlock_three():
    fin = open('words.txt')
    word_list = [line.strip() for line in fin]
    for line in word_list:
        word = line.strip()
        if in_bisect(word_list, word[::3]) and in_bisect(word_list, word[1::3]) and in_bisect(word_list, word[2::3]):
            print (word, word[::3], word[1::3], word[2::3])

##interlock_three()


##checks whether a word has (n) interlocking words within it
def interlock_n(word, n):
    fin = open('words.txt')
    word_list = [line.strip() for line in fin]
    count = 0
    for i in range(n):
        interlock = word[i::n]
        print (interlock)
        if in_bisect(word_list, interlock):
            count += 1
    if count == n:
        return True
    else:
        return False

##print(interlock_n("separated", 3))




