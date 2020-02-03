import random

lll = random.sample([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
result = [[0 for i in range(10)] for j in range(1 << 10)]

n = len(lll)

for i in range(1 << n):
    for j in range(n + 1):
        if i & (1 << j):
            result[i].append(lll[j])

for i in result:
    if sum(i) == 0:
        print('존재')
        break
else:
    print('무존재')

