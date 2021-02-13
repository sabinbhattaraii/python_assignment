'''
Write a Python program to slice a tuple
'''

tuples = ('A','s','s','i','g','n','m','e','n','t')
start = int(input('Enter number from 1-10 :'))
stop = int(input('Enter number from 1-10 :'))
new_tuple = tuples[start:stop]
print(new_tuple)