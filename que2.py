z=[1,2,3,4,5,6,7,8,9,10]
dic={}
d={}
c=1
count=1
for i  in z:
    if i%2==0:
        dic['even'+str(c)]=z
        count=count+1
    else:
        d['odd'+str(c)]=i
        c=c+1
print(dic)
print(d)
