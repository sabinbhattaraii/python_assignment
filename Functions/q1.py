'''
Write a Python function to find the Max of three numbers.
'''


def Max(first,second,third):
    if first > second and first > third:
        return (f"The max number is {first}") 
    elif second > first and second > third:
        return (f"The max number is {second}")
    else:
        return (f"The max number is {third}") 

first = int(input("enter first number :"))
second = int(input("enter second number :"))
third = int(input("enter third number :"))

print(Max(first,second,third))
