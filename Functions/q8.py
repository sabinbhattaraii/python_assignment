'''
Write a Python function that takes a list and returns a new list with unique
elements of the first list.
Sample List : ​ [1,2,3,3,3,3,4,5]
Unique List : ​ [1, 2, 3, 4, 5]
'''

def unique(lists):
    new_list = []
    for x in lists:
        if x not in new_list:
            new_list.append(x)
    return new_list

#lists = list(input('Enter a list : '))
#print(unique(lists))
print(unique([1,2,3,3,3,3,4,5]))