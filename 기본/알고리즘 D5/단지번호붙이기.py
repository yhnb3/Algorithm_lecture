T = int(input())
s = [[0] * (T + 2) for i in range(T + 2)]
count = 0


def find_danzi(a, b):
    s[a][b] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        if s[a + dx[i]][b + dy[i]] == 1:
            find_danzi(a + dx[i], b + dy[i])
            global count
            count += 1
    return count


for i in range(1, T + 1):
    a = [int(x) for x in input()]
    # print(a)
    for j in range(1, T + 1):
        s[i][j] = a[j - 1]

result = []
for j in range(T + 2):
    for h in range(T + 2):
        if s[j][h] == 1:
            count = 1
            result.append(find_danzi(j, h))
print(len(result))

for i in range(len(result)):
    print(sorted(result)[i])
