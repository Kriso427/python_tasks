def most_frequent(string):
    string_dict = {}
    for letter in string:
        if not letter.isalpha():
            continue
        if letter not in string_dict:
            string_dict[letter] = 1
        elif letter in string_dict:
            string_dict[letter] += 1
    sorted_string_dict = sorted(string_dict, key=string_dict.get, reverse=True)
    return sorted_string_dict

print(most_frequent("Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages."))
