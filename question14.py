# a={"geetu":90,"raju":60,"sapna":70,"pinki":34,"renu":45,"ram":67}
# for i in a:
#     for j in a:
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)



# a={"mama":12,"tinku":34,"kalu":45,"rani":56}
# for i in a:
#     for j in a:
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)



a={"mama":12,"tinku":84,"kalu":5,"rani":56}
b=sorted(a.values())
# print(b)
d={}
for i in b:
    for j in a.keys():
        if a[j]==i:
            d[j]=i
            break
print(d)
b = sorted(a.values(),reverse=True)
d = {}
for i in b:
    for j in a.keys():
        if a[j] == i:
            d[j] = i
            break
print(d)
