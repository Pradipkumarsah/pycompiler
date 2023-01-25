# s={10,30,40}
# print(s)
# s.add(29)
# s.add(333)
# print(s)
# s.update([100,200,930],'durga',range(1,4))
# print(s)
# s.add('python')
# s.update('python')
# print(s)

# s={10,30,40}
# s2=s
# s1=s.copy()
# print(type(s1),id(s1),id(s),id(s2))

# print(s.pop())
# print(s.pop())
# print(s.pop())


# s.discard(30)
# print(s)
# s.clear()
# print(s)

# s1={10,30,20,40}
# s2={40,50,60,23}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

# t1='durga'
# print(t1)
# print('d' in t1)
# print('z' in t1)

# s={x*x for x in range(6)}
# print(s)

# l=eval(input("Enter some list:"))
# l1=[]
# for x in l:
#     if x not in l1:
#         l1.append(x)
# print(l1)

w=input('Enter some word')
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)
print("The different vowels present in the given word:",d)
print('total no. of vowels',len(d))