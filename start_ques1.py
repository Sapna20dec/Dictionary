dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 2: 40}
dic3 = {5: 50, 6: 60}
dic = {}
for i in dic1:
    for j in dic2:
        for k in dic3:
            if i == j:
                dic[i] = dic1[i]+dic2[j]
            else:
                dic[i] = dic1[i]
                dic[j] = dic2[j]
                dic[k] = dic3[k]
print(dic)
