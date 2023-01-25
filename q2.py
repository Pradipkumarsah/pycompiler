# # # i=0
# # # while -122:
# # #     print("hello")
# # #     i+=1
# # #     if i==5:
# # # #         break
# # # for i in range(10):
# # #     if i==7:
# # #         print("it is done")
# # #         break
# # # #     print(i)
cart=[10,20,70,80,90]
for item in cart:
        if item>500:
            print("sorry, we can't process this order.")
            break
        print("processing item.",item)
else:
    print("congrats...all items are processed.")
# # # for i in range(10):
# # #     if i%2==0:
# # #         continue
# # #     print(i)
# numbers=[10,20,30,0,50,30]
# for n in numbers:
#     if n==0:
#         print("not divisible by 0.")
#         continue
#     print("100/{}={}".format(n,100/n))
