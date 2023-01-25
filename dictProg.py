# d=eval(input("Enter the dictionary:"))
# s=sum(d.values())
# print("The sum is:",s)

#sum is applicable for list,tuple ,set and dictionary.
#no of occurences of each letter present in the given string.

# word=input("Enter string:")
# d={}
# for x in word:
#     d[x]=d.get(x,0)+1
# for k,v in sorted(d.items()):
#     print("{} occured {} times.".format(k,v))


# word=input("Enter string:")
# vowel={'a','e','i','o','u'}
# d={}
# for x in word:
#     if x in vowel:
#         d[x]=d.get(x,0)+1
# for k,v in sorted(d.items()):
#     print("{} occured {} times.".format(k,v))


# n=int(input("Enter the number of students:"))
# d={}
# for i in range(n):
#     name=input("Enter student name:")
#     marks=int(input("Enter the student's mark:"))
#     d[name]=marks
# print(d)
# while True:
#     name=input("Enter student Name to get marks:")
#     marks=d.get(name,-1)
#     if marks==-1:
#         print("student not available.")
#     else:
#         print("The marks of {} : {}".format(name,marks))
#     option=input("Do you want to find another students mark [yes/no]: ")
#     if option=='no':
#         break
# print("Thank for using our application.")


# square={x:x*x for x in range(1,6)}
# for k,v in square.items():
#     print("Square of {} is : {}".format(k,v))