import copy


def rsa(arr, p):
    r = 0
    s = 0
    a = 0
    for i in range(p - 1):
        for j in range(80):
            if arr[i][j] == '(':
                r += 1
            elif arr[i][j] == ')':
                r -= 1
            elif arr[i][j] == '{':
                s += 1
            elif arr[i][j] == '}':
                s -= 1
            elif arr[i][j] == '[':
                a += 1
            elif arr[i][j] == ']':
                a -= 1
        abc.append([r, s, a])


def cc(arr, n):
    for i in range(1, n):
        cnt = 0
        for j in range(80):
            if arr[i][j] != '.':
                break
            cnt += 1
        tabs.append(cnt)


def m_c(arr, p):
    for r in range(1, 21):
        for s in range(1, 21):
            for a in range(1, 21):
                if p == 1:
                    arr.append([r, s, a])
                else:
                    if abc[0][0] * r + abc[0][1] * s + abc[0][2] * a == tabs[0]:
                        arr.append([r, s, a])
    for i in range(1, p - 1):
        ident = []
        for j in arr[:]:
            if j[0] * abc[i][0] + j[1] * abc[i][1] + j[2] * abc[i][2] == tabs[i]:
                ident.append([j[0], j[1], j[2]])
        arr = copy.deepcopy(ident)
    return arr


def last(arr, p):
    print('#{} {}'.format(tc, 0), end='')
    for i in range(p - 1):
        now = arr[0][0] * abc[i][0] + arr[0][1] * abc[i][1] + arr[0][2] * abc[i][2]
        for j in arr[1:]:
            if j[0] * abc[i][0] + j[1] * abc[i][1] + j[2] * abc[i][2] != now:
                now = -1
                break
        print(' {}'.format(now), end='')
    print()


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pro = [[0] * 80 for i in range(N)]
    me = [[0] * 80 for i in range(M)]
    for i in range(N):
        a = input()
        for j in range(len(a)):
            pro[i][j] = a[j]
    for i in range(M):
        a = input()
        for j in range(len(a)):
            me[i][j] = a[j]
    abc = []
    RSA = []
    tabs = []
    rsa(pro, N)
    cc(pro, N)
    alist = m_c(RSA, N)
    abc.clear()
    tabs.clear()
    rsa(me, M)
    last(alist, M)
