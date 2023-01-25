# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(5))

# def sqr(n):
#     return n*n

# s=lambda n:n*n
# print(s(6))

#lambda input:express/expected output

# s=lambda a:a*a
# print(s(3))
# print(s(5))

# s=lambda a,b:a+b
# print("{} is the sum of {} and {}".format(s(3,4),3,4))

# s=lambda a,b:a if a>b else b
# print("{} is the biggest".format(s(6,55)))

# def iseven(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l=[0,3,4,5,6,78,787]
# l1=list(filter(iseven,l))
# print(l1)
# print(type(l1))


# l1=list(filter(lambda x:x%2==0,l))
# print(l1) 

# def double(a):
#     return a*a
# l=[1,2,3,4,5,6,7,8,9]
# l1=list(map(double,l))
# print(l1)

l=[2,3,4,5,6,7]
l1=tuple(map(lambda a:a*a,l))
print(l1)

l2=[2,3,3,4,5,6]
l4=list(map(lambda x,y:x*y,l,l2))[4]
print(l4)

l3=[0,4,5,6,6,7,78,8]
l1=list(filter(lambda n:n%2==0,l3))
print(l1) 

l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)