'''Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t' '''


string = input('enter a string:')
lists = [string[0],string[1:]]
for x in lists[1]:
    if lists[0] == x:
        b = str(lists[1].replace(x,'$'))
        c = lists[0]+b
print(c)