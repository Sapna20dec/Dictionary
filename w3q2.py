user=input("enter a name")
s = user.split()
p = {}
c = 0
for i in user:
    p[c] = i
    c = c+1
print(p)






user=input("enter a name")
s=user.split()
p={}
c=0
z=" "
for i in user:
    p[c]=i
    z=('space'+str(c))
    c=c+1
print(p)
