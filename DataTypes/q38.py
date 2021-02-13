'''
Write a Python program to remove a key from a dictionary.
'''

dic = {1:10,2:20,3:30,4:40,5:50,6:60,7:70,8:80,9:90}
number = int(input("Enter a number from 1 to 9 to delete"))
if number in dic:
    del dic[number]
print(dic)