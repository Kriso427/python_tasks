import string

def strip(file):
    fin = open(file)
    cleaned_words = []

    for line in fin:
        for word in line.split():
            word = word.strip(string.whitespace + string.punctuation)
            word = word.lower()

            if word:
                cleaned_words.append(word)

    return cleaned_words

