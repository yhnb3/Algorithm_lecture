def uf(y):
    if y == cycle[y]:
        return y
    else:
        return uf(cycle[y])


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    i_x = list(map(int, input().split()))
    i_y = list(map(int, input().split()))
    e = float(input())
    krus = []
    cycle = [0] * N
    for i in range(N):
        cycle[i] = i
    for i in range(N):
        for j in range(i + 1, N):
            krus.append([(i_x[i] - i_x[j]) ** 2 + (i_y[i] - i_y[j]) ** 2, i, j])
    r_krus = sorted(krus)
    ans = 0
    cnt = 0
    for i in range(0, len(r_krus)):
        if r_krus[i][1] != uf(r_krus[i][2]):
            cycle[r_krus[i][2]] = r_krus[i][1]
            ans += r_krus[i][0]
            cnt += 1
        if cnt == N - 1:
            break

    print('#{} {}'.format(test_case, int(ans * e)))


