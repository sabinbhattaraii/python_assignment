'''
Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.
'''

def factorial(number):
    if number > 0:
        factorial = 1
        for x in range(1,number+1):
            factorial *= x 
        return factorial
    else:
        print("Negative number can't have factorial")

number  = int(input('Enter a number'))
print(factorial(number))