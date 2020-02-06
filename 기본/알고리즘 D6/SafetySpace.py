import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open('SafetySpace.txt')

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ss = [[0]*(T + 2) for i in range(T + 2)]
ss_test = [[0]*(T + 2) for i in range(T + 2)]
for i in range(1, T + 1):
    a = list(map(int, input().split()))
    for j in range(1, T + 1):
        ss[i][j] = a[j-1]


def rain(a, b):
    ss_test[a][b] = 0
    for i in range(4):
        if ss_test[a + dx[i]][b + dy[i]] != 0:
            rain(a + dx[i], b + dy[i])


me = 0
max_num = 0

while 1:
    count = 0
    for i in range(T + 2):
        ss_test[i] = ss[i][:]

    for i in range(1, T + 1):
        for j in range(1, T + 1):
            if ss_test[i][j] <= me:
                ss_test[i][j] = 0

    if max(max(ss)) == me:
        break

    for i in range(1, 1 + T):
        for j in range(1, T + 1):
            if ss_test[i][j] != 0:
                rain(i, j)
                count += 1
    if max_num < count:
        max_num = count

    me += 1

print(max_num)