'''
​Write a Python program to change a given string to a new string where the first
and last chars have been exchanged.
'''

string = list(input('enter a string:'))
first = list(string[0])
middle = list(string[1:-1])
last = list(string[-1])
print(''.join(last+middle+first))