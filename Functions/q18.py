'''
Write a Python program to check whether a given string is number or not
using Lambda.
'''

string = str(input('Enter a string'))
check = lambda x : True if x in ['0','1','2','3','4','5','6','7','8','9'] else False
print(check(string))