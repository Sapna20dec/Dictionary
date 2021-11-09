a=[3,4,3,6,8,37,4]
b=[4,5,6,7,8,5,4]
c={}
for i in a:
    for j in b:
        c[i]=(j)
        b.remove(j)
        break
print(c)