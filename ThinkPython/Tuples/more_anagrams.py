def more_anagrams():
    word_d = {}
    fin = open('words.txt')
    word_list = [line.strip() for line in fin]
    for word in word_list:
        word_d.setdefault(tuple(sorted(word)), []).append(word)

    sorted_word_d = sorted(word_d, key=lambda k: len(word_d[k]), reverse=True)

    for key in sorted_word_d:
        if len(word_d[key]) > 1 and len(key) == 8:
            print(key, word_d[key])

(more_anagrams())