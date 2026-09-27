def metathesis_pairs():
    word_d = {}
    fin = open('words.txt')
    word_list = [line.strip() for line in fin]
    for word in word_list:
        word_d.setdefault(tuple(sorted(word)), []).append(word)

    sorted_word_d = sorted(word_d, key=lambda k: len(word_d[k]), reverse=True)

    for key in sorted_word_d:
        if len(word_d[key]) > 1:
            for word1 in word_d[key]:
                for word2 in word_d[key]:
                    if sum(1 for i in range(len(word1)) if word1[i] != word2[i]) == 2:
                        if word1 < word2:
                            print(word1, word2)

metathesis_pairs()