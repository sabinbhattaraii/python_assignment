'''
Write a Python program to multiplies all the items in a list.
'''

mul = 1
lists = list(input('enter a list of items to mul :'))
for y in lists:
    if y == ' ' or y == "," or y == "'" or y == '"':
        lists.remove(y)
for x in lists:
    mul *= int(x) 
print(mul)