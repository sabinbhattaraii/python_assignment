'''
Write a Python function to create the HTML string with tags around the
word(s).
Sample function and result :add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
'''

def add_tags(tag,word):
    x = print(f'<{tag}>{word}</{tag}>')
    return x 

tag = input('Enter the tag:')
word = input('Enter the string:')
add_tags(tag,word)