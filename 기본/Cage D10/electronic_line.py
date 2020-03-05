# N = int(input())
# L = [list(map(int, input().split())) for i in range(N)]
N = 100
L = []
check = [[] for i in range(N)]
# cache = [[None] * (1 << N) for i in range(N)]
for i in range(1, N + 1):
    c = [i, i]
    for j in range(1, N + 1):
        L.append(c)


def iscross():
    for i in range(N):
        for j in range(N):
            if L[i][0] < L[j][0] and L[i][1] > L[j][1]:
                check[i].append(j)
            elif L[i][0] > L[j][0] and L[i][1] < L[j][1]:
                check[i].append(j)
    return


iscross()


def line(n, visit, cnt):
    for i in check[n]:
        if cnt & (1 << i) == 0:
            cnt = cnt | (1 << i)
    if visit == (1 << N) - 1:
        return 1
    # if cache[n][visit]:
    #     return cache[n][visit]

    ret = 1
    for i in range(N):
        if visit & (1 << i) == 0:
            if cnt & (1 << i) == 0:
                ret = max(ret, line(i, visit | (1 << i), cnt) + 1)
    # cache[n][visit] = ret
    return ret


result = []
max_num = 0
for i in range(N):
    a = line(i, 1 << i, 0)
    if max_num < a:
        max_num = a

print(N - max_num)