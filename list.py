# l=[1,2,3,4,5,6,7,7,8,9]
# # i=0
# # for x in l:
# #         print("{} is present at +ve index {} and -ve index at {}".format(x,i,i-len(l)))
# #         i+=1

# print(len(l))
# print(l.count(7))
# if 70 in l:
#     print(l.index(70))
# else:
#     print("not available.")
# l.append(100)
# l.append(200)
# print(l)
# l1=['chicken','mutton','fish']
# l2=['KF','Rc','fo']
# l1.extend(l2)
# print(l1)

# l=[20,10,8,9,0,2,1]
# l.sort(reverse=True)
# print(l)

# s='durgasoftdurgasoft'
# print(s.find('soft'))
# print(s.find('abc'))
# print(s.rfind('soft'))
# print(s.find('a',5,10))
# print(s.rindex('a'))
name='durga'
# age=48
# salary=10000
# print("{}'s age is {} and hsi salary is :{}".format(name,age,salary))
# print("{0}'s age is {1} and hsi salary is :{2}".format(name,age,salary))
# print("{x}'s age is {y} and hsi salary is :{z}".format(z=salary,x=name,y=age))

#s=input("Enter some string:")

# print(s[::-1])
# print(''.join(reversed(s)))
# for x in reversed(s):
#     print(x,end='')
# i=len(s)-1
# output=''
# while i>=0:
#     output=output+s[i]
#     i=i-1
# print(output)
# l=s.split()
# print(l)
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i=i-1
# output=' '.join(l1)
# print(output)

# l=s.split()
# l1=[]
# for x in l:
#     l1.append(x[::-1])
# output=' '.join(l1)
# print(output)

# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# print(''.join(l))

# print(''.join(set(s)))

# d={}
# for x in s:
#     if x not in d.keys():
#         d[x]=1
#     else:
#         d[x]=d[x]+1
# print(d)
# for k, v in d.items():
#     print("{}'s character occurs={}times".format(k,v))

list=[1,2,3,4,5,5,6]
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1

# for x in list:
#     if x%2==0:
#         print(x)
        
# l=['a','b','c','d','e']
# x=len(l)
# for i in range(x):
#     print(list[i],'is available at +ve index:',i,'and -ve index at:',i-x)

#extend methods
# l1=['chicken','mutton','fish']
# l2=['kf','rc','fo']
# l1.extend(l2)
# print(l2)
# l1.extend('durga')
# l1.append('durga')
# print(l1)

#remove () functions
# l3=[10,20,30,40]
# x=int(input("Enter the element to be removed:"))
# if x in l3:
#     l3.remove(x)
#     print(x,'is removed successfully.')
# else:
#     print("not available.")

#pop() functions
#l1=[10,20,30,40,50]
# print(l1.pop())
# print(l1.pop(3))
# print(l1)
# l1.reverse()
# print(l1)

#according to default sorting method
#numbers=>ascending order
#abc=alphabetically
l1=[30,10,50,28,40]
# l2=['boy','cat','apple','Cat','90']
# l2.sort()
# print(l2)
# l1.sort()
# print(l1)

#to sort in reverse of natural sorting order.i.e. descending order
l1.sort(reverse=False)
# print(l1)
# x=[10,20,30,50]
# y=x
# y[1]=33
# print(id(x))
# print(id(y))
# print(x)

# x=[10,30,40]
# y=x[:]
# z=x.copy()
# y[1]=44
# print(x)
# print(y)
# print(z)
# print(id(z))
# print(id(x))
# print(id(y))

# a=[10,20,30,40]
# b=[50,60,70]
# c=a.extend(b)
# d=a+[30]
# e=a*2
# d.sort(reverse=True)
# print("a:",a)
# print("b:",b)
# print("c:",c)
# print('d:',d)
# print('e:',e)
# x=a==b
# print(x)

a=[10,30,78]
b=[10,30,99]
c=a is b
d=a==b
print(c,d)
print(a>= b)