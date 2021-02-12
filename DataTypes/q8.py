'''
Write a Python program to remove the n​ th​ index character from a nonempty
string.
'''

string = str(input('enter a string :'))
index = int(input('enter a intege index'))
if index < len(string):
    first = string[:index]
    second = string[index+1:]
    print(first+second)
else:
    print("Given index does not exist")