# sum=0
# for i in range(1,101):  
#     if i%2!=0:
#         sum=sum+i
# print("sum of 1 to 100 odd number is:",sum)       
n=5

# for i in range (5,0,-1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for j in range(0,2*i-1):
#         print("* ", end="") 
#     print(end="\n")   


n=5
for i in range(1,n+1):
    for j in range(i):
        print((chr(64+i)),end=" ")
    print("\n")