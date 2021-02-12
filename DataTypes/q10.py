'''
Write a Python program to remove the characters which have odd index
values of a given string.
'''
string = input('Enter a string')
new_string = ""
for x in range(len(string)):
    if x % 2 == 0:
        new_string += string[x]
print(new_string)
        