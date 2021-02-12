'''
Write a Python function that takes a list of words and returns the length of the
longest one.
'''


def longest():
    string = input("enter a list of words:")

    long = 0 

    for word in string.split():
        if len(word) > long:
            long = len(word)
    print('The longest words length is :',long)

longest()