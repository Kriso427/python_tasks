def palindrome(word):
    return word == word[::-1]

for i in range(100000, 999996):
    if palindrome(str(i)[-4:]) and palindrome(str(i+1)[-5:]) and palindrome(str(i+2)[1:5]) and palindrome(str(i+3)):
        print(i)

