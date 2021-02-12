'''
Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
'''

def mul(number):
    inputs = int(input('Enter a number :'))
    return number * inputs

print(mul(15))