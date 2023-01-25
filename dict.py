# d={}
# s=dict()
# print(type(d),type(s))
# d[100]='durga'
# d[200]='ravi'
# d[300]='chone'
# print(d)
# d={'a':'apple','b':'ball'}
# print(d)

# n=int(input('Enter the number of students:'))
# i=1
# rec={}
# while i<=n:
#     name=input('Enter student name:')
#     marks=input('Enter % of marks:')
#     rec[name]=marks
#     i+=1
# print("Name of student:\t","% of Marks")
# for x in rec:
#     print("\t",x,"\t\t",rec[x])

#how to update dictionaries:
d={101:'durga',102:'ravi',103:'shive'}
# d[101]='sunnyLeone'
# d[104]='depika'
# print(d)

#how to delete dictionaries:
# del d[10]
# print(d)

# d.clear()
# print(d)
# d[444]='pk'
# print(d)
# del d
# print(d)

# Assingning multiple values to the single key.
# list=['durga','shive','ram']
# d[100]=list
# print(d)

# d={}
# t=dict({20:'durga',33:'ram'})
# print(t)

# dc=dict([(100,'durga'),(23,'margo')])
# print(dc)

# cc=dict([[100,'durga'],[23,'margo']])
# print(cc)
# print(len(cc))
# print(cc.get(100))
# print(cc.get(300,'pradip'))
# print(cc.pop(100))
# print(cc)
# print(cc.popitem())
# print(cc)

# print(cc.keys())
# for k in cc.values():
#     print(k)

#items--------
d={100:'surya',200:'arun',300:'krishna',400:'shiva'}
list=d.items()
print(list)
print()
for k,v in list:
    print(k,'....',v)
    
# d.pop()
# print(d)

# d1=d.copy()
# d.setdefault(1000,'pradip')
# print(d)

#update---------
