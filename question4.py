dic = {
    1: 'NAVGURUKUL',
    2: 'IN',
    3: {
        'A': 'WELCOME',
        'B': 'To',
        'C': 'DHARAMSALA'
    }
}

for i, j in dic.items():
    if i == 3:
        j.pop('A')
print(dic)
