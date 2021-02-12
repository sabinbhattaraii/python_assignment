'''
Write a Python program to reverse a string.
Sample String ​ : "1234abcd"
Expected Output ​ : "dcba4321"
'''

def reverse(string):
    lists = list(string)
    lists.reverse()
    return (''.join(lists))

print(reverse('1234abcd'))