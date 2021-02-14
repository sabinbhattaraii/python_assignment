'''
Write a Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''

string=str(input('Enter the string?'))
if 'not' in string and 'poor' in string and string.find('not') < string.find('poor'):
    string.replace('not','')
    string.replace('poor','good')
print(string)