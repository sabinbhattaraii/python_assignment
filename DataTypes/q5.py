'''
Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''


word = str(input('enter a string:'))
if len(word) < 3 :
    print(word)
else :
    new_word = word[-3:]
    if new_word == "ing":
        print(word+"ly")
    else :
        print(word+"ing")