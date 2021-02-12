'''Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz' '''

first = input('Enter first string')
second = input('Enter second string')

new_first = second[:2] + first[2:]
new_second = first[:2] + second[2:]

print(new_first + ' ' + new_second)
