'''
Write a Python program to multiply all the items in a dictionary.
'''

dictionary = {'English':80,'Nepali':97,'Social':88,'Maths':95,'Science':84,'Computer':91}
product = 1
for x in dictionary.values():
    product *= x 
print(product)