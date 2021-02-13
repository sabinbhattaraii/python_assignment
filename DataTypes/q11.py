'''
Write a Python program to count the occurrences of each word in a given
sentence.
'''

word = str(input('enter a sentence :'))
word_lists = list(word)
dict = {}
for x in word_lists:
    keys = dict.keys()
    if x in keys:
        dict[x] += 1
    else:
        dict[x] = 1

print(dict)
