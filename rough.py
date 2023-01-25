# # print("This is \" double\" ' qou'te symobol")
# s=input("Enter the name:")
# i=0
# for x in s:
#     print("The character at positive index {} and at negative index {} is :{}".format(i,i-len(s),x))
#     i+=1
s="Learning python is very easy."
# n=len(s)
# i=0
# while(i !=n):
#     print("{} in forward and {} in backward.".format(s[i],s[i-n]))
#     i+=1
# print(s[::])
# print(s[::-1])
# i=0
# while(i<len(s)):
#     print(s[i],end="")
#     i+=1
# print()
# print("data in backward direction:")
# j=len(s)-1
# while(j>0):
#     print(s[j],end='')
#     j-=1
# s=input("Enter main string")
# subs=input("Enter substring to search:")
# if subs in s:
#     print(subs,"it is found.")
# else:
#     print(subs,"not found.")
# s=input("Enter string1:")
# s2=input("Enter string2:")
# if s==s2:
#     print("both string are equal.")
# elif s<s2:
#     print("First string is smallwer than seocnd string.")
# else:
#     print("first string is bigger than second string.")
# city=input("Enter city name:")
# list=['Hyderabad','delhi','bangalore']
# if city.lstrip() in list:
#     print(city,"is present.")
# else:
#     print(city,"not available.")

# s=input("Enter main string:")
# subs=input("Enter substring:")
# flag=False
# pos=-1
# count=0
# n=len(s)
# while True:
#     pos=s.find(subs,pos+1,n)
#     if pos==-1:
#         break
#     print("found at index",pos)
#     count+=1
#     flag=True
# if flag==False:
#     print("not found.")
# print("The number of occurences is :",count)
# print(s.count('n',8,15))
# s.replace("is","are")
# print(s)
# s1=s.replace("is","are")
# print(s)
# print(id(s))
# print(id(s1))
# sp=s.split()
# for x in sp:
#     print(x)
# date="12-12-2000"
# #print(date)
# d=date.split('-')
# for x in d:
#     print(d)
# s="durga software solutions hyderabad india."
# sp=s.split(' ',3)
# sp1=s.rsplit(' ',3)
# for x in sp:
#     print(x)
    
# t=('Pradip','kuMar','saH')
# s='-'.join(t)
# print(s)
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# a='learning python is very easy.'
# print(a.startswith('learning'))
# print(a.endswith('easy.'))
# print("character at even position:",s[::2],sep=' ')
# print("character at odd position:",s[1::2],sep=" ")

# i=0
# print("character at even position:")
# while i<len(a):
#     print(a[i],end=' ')
#     i+=2
# print()  
# j=1  
# print("character at odd position:")
# while j<len(a):
#     print(a[j],end=' ')
#     j+=2
# print()
# x=input("Enter some string:")
# s1=s2=output=''
# for b in sorted(x):
#     if b.isalpha():
#         s1+=b
#     else:
#         s2+=b
# print(s1)
# print(s2)
# for x in sorted(s1):
#     output+=x
# for x in sorted(s2):
#     output+=x
# print(output)

# print()

# s=input("Enter some string:")
# output=''
# for x in s:
#     if x.isalpha():
#         output+=x
#         prev=x
#     else:
#         output=output+prev*(int(x)-1)
# print(output)
# s=input("Enter some string:")
# output=''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         prev=x
#     else:
#         output=output+chr(ord(prev)+int(x))
# print(output)

# s1=input("ENter 1st string:")
# s2=input("ENter 2nd string:")
# i=j=0
# output=''
# while i<len(s1) or j<len(s2):
#     output=output+s1[i]+s2[j]
#     i+=1
#     j+=1
# print(output)
# print()

# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         output=output+s1[i]
#         i+=1
#     if j<len(s2):
#         output=output+s2[j]
#         j+=1
# print(output)

# x=[10,30,40]
# x.clear()
# print(x)

# x=[10,30,40,[50,60]]
# print(x)
# print(x[0])
# print(x[3][0])

# x=[[10,20,30],[40,50,60],[70,80,90]]
# print(x)
# print("Elements Row wise:")
# for a in x:
#     print(a)
# print('element in matrix style:')
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         print(x[i][j],end=' ')
#     print()
    
# # l1=[]
# # for x in range(1,11):
# #     l1.append(x*x)
# # print(l1)

# l1=[x*x for x in range(1,11)]
# print(l1)
# l2=[ x for x in l1 if x%2==0]
# print(l2)

# words=['Bala','Chana','Gana','Ana']

# list=[x**2 for x in range(1,11) if (x**2)%2!=0]
# print(list)
# list2=[x for x in list if x%2!=0]
# print(list2) 

# words=['Balaiah','Nag','venkatesh','chiru']
# l=[w for w in words if (len(w))<6]
# print(l)
# fL=[w[0] for w in words]
# print(fL)

# n1=[10,20,30,40]
# n2=[30,40,50,60]
# n=[nm for nm in n1 if nm not in n2]
# print(n)

# words="the quick brown fox jumps over the lazy dog".split()
# print(words)

# l=[[w.upper(),len(w)] for w in words]
# print(l)

vowels=['a','e','i','o','u']
word=input("Enter some string :")
found=[]
for letter in word:
    if letter.lower() in vowels:
        if letter not in found:
            found.append(letter.lower())
print(found)
print("The number of different vowels present in ",word, "is:",len(found))
