'''
Write a Python program to print the even numbers from a given list.
Sample List : ​ [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result ​ : [2, 4, 6, 8]
'''

def even(lists):
    new_list = []
    for item in lists:
        if item % 2 == 0:
            new_list.append(item)
    return new_list 

print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    
