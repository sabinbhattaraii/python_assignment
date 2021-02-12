'''
​ Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
'''

def insert_string_middle(symbol,string):
    x = print(f'{symbol[:2]}{string}{symbol[2:]}')
    return x 

symbol = input('Enter the symbol:')
string = input('Enter the string:')
insert_string_middle(symbol,string)

