import string
import re

def remove_punctuation(text):
    return re.sub(r'[^\w]', '', text)

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
                    word = remove_punctuation(word)
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


    not_in_words = []
    fin = open('words.txt')
    word_list = [line.strip() for line in fin]

    for word in cleaned_words:
        if word not in word_list:
            not_in_words.append(word)
    print("words that are not in words.txt are", not_in_words)

count_words("book.txt")