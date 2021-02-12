'''
Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
'''

words = input("enter sequence of words :")
lists = [lists for lists in words.split(",")]
print(",".join(sorted(lists)))