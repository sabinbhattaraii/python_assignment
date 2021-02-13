'''
Write a Python program to check whether all dictionaries in a list are empty or
not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
'''

my_list = [{},{},{}]
for item in my_list:
    if (not item) :
        output = True
    else:
        output = False
print(output)

my_list1 = [{1,2},{},{}]
for item in my_list1:
    if (not item) :
        output = True
    else:
        output = False
print(output)