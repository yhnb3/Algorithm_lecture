import sys
sys.stdin = open('2048.txt')

T = int(input())

for test_case in range(1, T + 1):
    a, check = map(str, input().split())
    num = int(a)
    ss = [[0]*(num+2) for i in range(num+2)]

    for i in range(1, num+1):
        b = list(map(int, input().split()))
        for j in range(1, num+1):
            ss[i][j] = b[j-1]

    if check == 'up':
        for i in range(1, num + 1):
            for j in range(1, num + 1):
                if ss[j][i] == 0:
                    continue
                else:
                    for k in range(1, num - j + 1):
                        if ss[j + k][i] == 0:
                            continue
                        else:
                            if ss[j + k][i] == ss[j][i]:
                                ss[j][i] = ss[j][i] * 2
                                ss[j + k][i] = 0
                            break

        for i in range(1, num + 1):
            for j in range(1, num):
                if ss[j][i] == 0:
                    for k in range(1, num - j + 1):
                        if ss[j + k][i] == 0:
                            continue
                        else:
                            ss[j][i], ss[j+k][i] = ss[j+k][i], ss[j][i]
                            break
                else:
                    continue

    elif check == 'left':
        for i in range(1, num + 1):
            for j in range(1, num + 1):
                if ss[i][j] == 0:
                    continue
                else:
                    for k in range(1, num - j + 1):
                        if ss[i][j + k] == 0:
                            continue
                        else:
                            if ss[i][j+k] == ss[i][j]:
                                ss[i][j] = ss[i][j] * 2
                                ss[i][j+k] = 0
                            break

        for i in range(1, num + 1):
            for j in range(1, num):
                if ss[i][j] == 0:
                    for k in range(1, num - j + 1):
                        if ss[i][j + k] == 0:
                            continue
                        else:
                            ss[i][j], ss[i][j + k] = ss[i][j + k], ss[i][j]
                            break
                else:
                    continue

    elif check == 'down':
        for i in range(1, num + 1):
            for j in range(num, 0, -1):
                if ss[j][i] == 0:
                    continue
                else:
                    for k in range(1, j):
                        if ss[j - k][i] == 0:
                            continue
                        else:
                            if ss[j-k][i] == ss[j][i]:
                                ss[j][i] = ss[j][i] * 2
                                ss[j-k][i] = 0
                            break

        for i in range(num, 0, -1):
            for j in range(num, 1, -1):
                if ss[j][i] == 0:
                    for k in range(1, j):
                        if ss[j-k][i] == 0:
                            continue
                        else:
                            ss[j][i], ss[j-k][i] = ss[j-k][i], ss[j][i]
                            break
                else:
                    continue

    elif check == 'right':
        for i in range(1, num + 1):
            for j in range(num, 0, -1):
                if ss[i][j] == 0:
                    continue
                else:
                    for k in range(1, j):
                        if ss[i][j - k] == 0:
                            continue
                        else:
                            if ss[i][j - k] == ss[i][j]:
                                ss[i][j] = ss[i][j] * 2
                                ss[i][j - k] = 0
                            break

        for i in range(1, num + 1):
            for j in range(num, 1, -1):
                if ss[i][j] == 0:
                    for k in range(1, j):
                        if ss[i][j - k] == 0:
                            continue
                        else:
                            ss[i][j], ss[i][j - k] = ss[i][j - k], ss[i][j]
                            break
                else:
                    continue

    print('#{}'.format(test_case))
    for i in range(1, 1 + num):
        for j in range(1, num + 1):
            print(ss[i][j], end=' ')
        print('')
