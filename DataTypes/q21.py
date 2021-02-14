'''
Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

lists = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
dic={}
new_list=[]
for item in lists:
    dic[item[1]]=item[0]
for i in sorted(dic):
    new_list+=list(tuple(dic[i],i))
print(new_list)