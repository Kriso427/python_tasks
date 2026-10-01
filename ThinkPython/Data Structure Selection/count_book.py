import string

def count_words(file):
    fin = open(file, encoding='utf-8')
    cleaned_words = []
    started = False
    ended = False

    for line in fin:
        if '*** START' in line:
            started = True
            continue
        if '*** END' in line:
            ended = True
        if started:
            for word in line.split():
                if ended:
                    break
                else:
                    word = word.strip(string.whitespace + string.punctuation)
                    word = word.lower()

                    if word:
                        cleaned_words.append(word)

    total_words = len(cleaned_words)
    print ("There is a total of", total_words , "words in the book")

    word_freq = {}
    for word in cleaned_words:
        word_freq[word] = word_freq.get(word, 0) + 1
    total_word_freq = len(word_freq)
    print ("There is a total of", total_word_freq , "Unique words")

    sorted_word_freq = sorted(word_freq, key=word_freq.get, reverse=True)
    print ("The top 10 most frequent words in the book are", sorted_word_freq[:10])

count_words("book.txt")