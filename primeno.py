# n=int(input("enter a number"))
# i=0
# k=1
# i=1
# d={}
# while k<=n:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c=c+1
#         j=j+1
#     if c==2:
#         d[k]=i
#         k=k+1
#     i=i+1
# print(d)

n=int(input("enter the number"))
k=1
c=0
d={}
i=1
while k<=n:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        d[k]=i
        k=k+1
    i=i+1
print(d)





