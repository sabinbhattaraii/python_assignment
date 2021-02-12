'''
Write a Python program to get the largest number from a list.
'''

lists = input('enter a list :')
max = 0 
for x in lists:
    if int(x) > max:
        max = x 
print(max)