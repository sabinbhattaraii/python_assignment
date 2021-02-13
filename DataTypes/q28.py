'''
Write a Python script to add a key to a dictionary.Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''

def add(dic,add):
    dic.update(add)
    return dic

dic = dict(input("Enter a dictionary :"))
add = dict(input("Enter a dictionary to add:"))
print(add(dic,add))