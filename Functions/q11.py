'''
Write a Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result.
'''


add = lambda x : x + 15
number = int(input("Enter a number : "))
print(add(number))

mul = lambda x , y : x * y
first = int(input('Enter a number to multiply'))
second = int(input('Enter a number to multiply'))
print(mul(first,second))