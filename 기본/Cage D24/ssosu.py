T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    for i in range(M, 0, -1):
        if N % i == 0 and M % i == 0:
            N = N // i
            M = M // i
            break
    k = M
    flag = True
    for i in [2, 5]:
        if M % i == 0:
            k = k // i
        if k == 1:
            flag = False
            break
    if not flag:
        print('#{} {}'.format(tc, N / M))
    else:
        fflag = True
        namuji = []
        mok = []
        r = N
        temp = 0
        while 1:
            r = r * 10
            if r > M:
                mok.append(r // M)
                namuji.append(r % M)
                for i in range(len(namuji) - 2, -1, -1):
                    if namuji[i] == (r % M) and mok[i] == (r // M):
                        fflag = False
                        temp = i
                        break
                if not fflag:
                    break
                r = r % M
            else:
                mok.append(r // M)
                namuji.append(r % M)
                for i in range(len(namuji) - 2, -1, -1):
                    if namuji[i] == r and mok[i] == (r // M):
                        fflag = False
                        temp = i
                        break
                if not fflag:
                    break
        print('#{} {}.'.format(tc, N // M), end='')
        for i in range(temp):
            if namuji[i] == 0:
                continue
            else:
                print(mok[i], end='')
        print('(', end='')
        for i in range(temp, len(mok) - 1):
            print(mok[i], end='')
        print(')')





