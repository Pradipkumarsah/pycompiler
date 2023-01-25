# def add(a,b):
#     return a+b
# res=add(10,40)
# print('sum is :',res)
#the default return value is none.

# def f1():
#     print('hello')
# f1()
# print(f1())

# def evenodd(n):
#     if n%2==0:
#         print("{} number is even".format(n))
#     else:
#         print("odd")
        
# evenodd(23)
# evenodd(24)

# def fact(n):
#     res=1
#     while n>=1:
#         res=res*n
#         n=n-1
#     return res
# for i in range(1,5):
#     print("The factorial of {} is {}".format(i,fact(i)))
    

# def cal(a,b):
#     sum=a+b
#     dif=a-b
#     mul=a*b
#     div=a/b
#     return sum, dif,mul,div
# t=cal(100,50)
# print(type(t))
# print("The result are:")
# for x in t:
#     print(x)

#types of arguments:

# 1.positional arguments
# 2.keyword arguments
# 3.default arguments
# 4.variable length arguments
#1.
# def sub(a,b):
#     print(a-b)
# sub(50,40)

#2.
# def wish(name, msg):
#     print("hello",name ,msg)
# wish(name='durga',msg='good morning')
# wish(msg='good morning',name='durga')
# wish('durga',msg='good morning')
# wish('durga',msg='Good morning')

#3.
# def wish(marks,age,name='Guest',msg='good morning.'):
#     print("student name:",name)
#     print('student age:',age)
#     print('student marks',marks)
#     print("msg:",msg)

# wish(100,34,'ram')
# print()
# wish(age=34,marks=333)
# print()
# wish(age=45,name='hari')

# def wish(msg,name='guest'):pass
#4.

# def f1(*a):
#     print('var-arg functions:')
# f1()
# f1(2)
# f1(3,4)
# f1(333,34,4,4,5)

# def sum(name,*n):
#     sum=0
#     for x in n:
#         sum+=x
#     print("The sum by",name," :",sum)
# sum('durga')
# sum('ravi',1)
# sum('ram',3,4)
# sum('hari',4,5,6)
# sum('surya',3,4,5,6,7,8,9,0)

# print()
# def sum(*n,name):
#     sum=0
#     for x in n:
#         sum+=x
#     print("The sum by",name," :",sum)
# sum(name='durga')
# sum(1,name='ravi')
# sum(1,2,3,name='ram')
# sum(4,5,6,7,name='hari')
# sum(3,3,4,5,6,7,name='surya')

#keyword variable length arguments
def display(**kwargs):
    print("Record Info:")
    for k,v in kwargs.items():
        print(k,'....',v) 
display(name='durga',marks=100,age=23,gf='sunny')
display(name='surya',gf1='siksha',gf2='viksha',gf3='lekhsha') 