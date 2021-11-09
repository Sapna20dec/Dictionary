a = {

    'a': 50,

    'b': 58,

    'c': 56,

    'd': 40,

    'e': 100,

    'f': 20

}
m=0
for i in  a:
    if a[i]>m:
        m=a[i]
print(m)
sm=0
for i in a:
    if a[i]!=m:
        if a[i]>sm:
            sm=a[i]
print(sm)
max=0
for i in a:
    if a[i]!=m and a[i]!=sm:
        if a[i]>max:
            max=a[i]
print(max)