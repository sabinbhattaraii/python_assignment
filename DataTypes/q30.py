'''
Write a Python script to check whether a given key already exists in a
dictionary.
'''

dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
check = int(input("Enter a integer from 1-10:"))
if check in dictionary :
    print("The key is in the dictionary")
else:
    print("The key is not in the dictionary")