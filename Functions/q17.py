'''
Write a Python program to find if a given string starts with a given character
using Lambda.
'''

string = str(input('Enter a string:'))
character = str(input('Enter a character to check:'))
check = lambda string,character : True if character in string[0] else False
print(check(string,character))