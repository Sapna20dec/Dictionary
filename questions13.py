a = {

    'a': 50,

    'b': 58,

    'c': 56,

    'd': 40,

    'e': 100,

    'f': 20

}
m=0
for i in a:
    if i in a:
        m=a[i]
        b=i
print(b)
print(m)
sm=0
for i in a:
    if a [i]!=m:
        if a[i]>sm:
            sm=a[i]
            b=i
print(b)
print(sm)
max=0
for i in a:
    if a[i]!=m and a[i]!=sm:
        if a[i]>max:
            max=a[i]
            b=i
print(b)
print(max)