'''
Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.Sample String ​ : 'The quick Brow Fox'
Expected Output : ​
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def count(string):
    upper_case = 0
    lower_case = 0
    for x in string:
        if x.isupper():
            upper_case += 1
        elif x.islower():
            lower_case += 1
    print(f'No. of Upper case characters : {upper_case}')
    print(f'No. of Lower case Characters : {lower_case}')

string = str(input("Enter a string :"))
count(string)