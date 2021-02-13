'''
Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
'''

first = list(input("Enter the first list:"))
second = list(input("Enter the second list"))
first[-1:] = second
print(first)