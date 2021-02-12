'''
Write a Python function to multiply all the numbers in a list.
Sample List : ​ (8, 2, 3, -1, 7)
Expected Output ​ : -336
'''

def multiply(lists):
    mul = 1
    for x in lists:
        mul *= int(x)
    return mul

print(multiply((8,2,3,-1,7)))