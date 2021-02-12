'''
Write a Python program to square and cube every number in a given list of
integers using Lambda.
'''

numbers = [1,2,3,4,5,6,7,8,9,10]
square = list(map(lambda x : x ** 2 ,numbers))
cube = list(map(lambda x : x ** 3 , numbers))
print(square)
print(cube)