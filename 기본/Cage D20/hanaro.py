def f(c):
    if c != cycle[c]:
        cycle[c] = cycle[f(cycle[c])]
    return cycle[c]


def u(x, y):
    xx = f(x)
    yy = f(y)
    if rank[xx] > rank[yy]:
        rank[xx] += 1
        cycle[yy] = cycle[xx]
    elif rank[xx] < rank[yy]:
        rank[yy] += 1
        cycle[xx] = cycle[yy]
    else:
        rank[xx] += 1
        cycle[xx] = cycle[yy]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    i_x = list(map(int, input().split()))
    i_y = list(map(int, input().split()))
    E = float(input())
    rank = [0] * N
    krus = []

    for i in range(N):
        for j in range(i + 1, N):
            krus.append([(i_x[i] - i_x[j]) ** 2 + (i_y[i] - i_y[j]) ** 2, i, j])
    r_krus = sorted(krus)
    cycle = [i for i in range(N)]
    result = 0
    for i in range(len(r_krus)):
        ans, a, b = r_krus[i]
        if f(a) != f(b):
            u(a, b)
            result += ans

    print('#{} {}'.format(tc, int(round(result * E, 1))))


