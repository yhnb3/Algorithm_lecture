a, b = map(int, input().split())
s = [[int(x) for x in input()] for i in range(a)]
size = 0
cc = 0
ccc = 0
cccc = 0

if a > b:
    if b & 1:
        size = (b // 2) + 1
    else:
        size = b // 2
else:
    if a & 1:
        size = (a // 2) + 1
    else:
        size = a // 2

for i in range(size, 1, -1):
    cc = 0
    for k in range(a - ((i - 1) * 2 + 1) + 1):
        for j in range(i - 1, b - i + 1):
            count = 0
            for h in range(i):
                if s[(i - 1) * 2 - h + k][j-h] != 1 or s[(i - 1) * 2 - h + k][j+h] != 1:
                    break

                if s[h + k][j-h] != 1 or s[h + k][j+h] != 1:
                    break

                count += 1
            if count == i:
                cc += 1
    if cc > 0:
        ccc += 1
        print(i)
        break

for i in range(a):
    for j in range(b):
        cccc += s[i][j]

if ccc == 0:
    if cccc == 0:
        print(0)
    else:
        print(1)




