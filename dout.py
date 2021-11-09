a = {"a": [1, 2, 3, 4, 5], "b": [7, 8, 6, 9, 10]}
sum=0
for i in a:
    for j in a[i]:
        sum=sum+j
print(sum)
