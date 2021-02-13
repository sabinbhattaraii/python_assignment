'''
Write a Python program to remove an item from a tuple
'''

tuples= (1,2,3,4,5,6,7,8,9)
item = int(input("enter a item to delete from 1 to 9 "))
lists = list(tuples)
lists.remove(item)
new_tuple = tuple(lists)
print(new_tuple)