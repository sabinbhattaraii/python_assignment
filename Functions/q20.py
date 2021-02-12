'''
Write a Python program to find intersection of two given arrays using
Lambda.
'''

array1 = [1,2,3,4,5,6]
array2 = [4,5,6,7,8,9]
intersection = list(filter(lambda x : x in array1, array2))
print(intersection)