# # # # for i in range(4):
# # # #    for j in range(4):
# # # #       print("i={} and j={}".format(i,j))
# # # n=int(input("Enter number of rows:"))
# # # for i in range(1,n+1):
# # #    for j in range(1,i+1):
# # #       print("*",end=' ')
# # #    print()
# # n=int(input("Enter number:"))
# # for i in range(1,n+1):
# #    print('* '*i)
# n=int(input("enter number:"))
# for i in range(n):
# #   print('* '*n)
#    for j in range(n):
#       print('* ',end='')
#    print()
n=int(input("Enter number:"))
for i in range(n):
#   print('* '*(n-i))
   for j in range(n-i):
      print('*',end=' ')
   print()