'''
Write a Python program to sort a list of dictionaries using Lambda.
'''

marks = [{'ram':'English', 'marks':98}, {'sam':'Science', 'marks':90}, {'roy':'Maths', 'marks':97},{'joy':'English','marks':92}]
sorted_marks = sorted(marks, key = lambda x: x['marks'])
print(sorted_marks)