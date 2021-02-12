'''
Write a Python function to check whether a number is in a given range
'''


def check(number):
    if number in range(0,10):
        return ('The number is in the given range')
    else:
        return ('The number is not in the given range')

number = int(input("Enter the number :"))
print(check(number))