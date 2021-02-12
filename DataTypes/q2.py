'''Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.
Sample String : 'Python'
Expected Result : 'Pyon'
Sample String : 'Py'
Expected Result : 'PyPy'
Sample String : ' w'
Expected Result : Empty String'''


word = list(input('enter a string:'))
if word[0] == "'" and word[-1] == "'" or word[0] == '"' and word[-1] == '"':
    word.pop(0)
    word.pop(-1)
    if len(word) < 2 :
        print("Empty String")
    else:
        print(word[0]+word[1]+word[-2]+word[-1])
else:
    if len(word) < 2 :
        print("Empty String")
    else:
        print(word[0]+word[1]+word[-2]+word[-1])
