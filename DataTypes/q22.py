'''
Write a Python program to remove duplicates from a list.
'''

lists = list(input("Enter a list : "))
new_list = set(lists)
print(list(new_list))