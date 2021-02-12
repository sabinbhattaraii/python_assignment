'''
Write a Python program to sum all the items in a list.
'''

sum = 0 
lists = list(input('enter a list of items to sum :'))
for y in lists:
    if y == ' ' or y == "," or y == "'" or y == '"':
        lists.remove(y)
for x in lists:
    sum += int(x) 
print(sum)