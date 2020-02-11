import sys
sys.stdin = open('회문.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    s = [list(input()) for i in range(N)]

    result = []
    for k in range(N):
        for i in range(N - M + 1):
            flag = True
            for j in range(M // 2):
                if s[k][i + j] == s[k][-(N - M + 1 - i) - j]:
                    pass
                else:
                    flag = False
                    break

            if flag:
                result.append([k, i, 1])
                break
            flag = True
            for h in range(M // 2):
                if s[i + h][k] == s[-(N - M + 1 - i) - h][k]:
                    pass
                else:
                    flag = False
                    break

            if flag:
                result.append([k, i, 2])
                break

        if flag:
            break

    print('#{} '.format(test_case), end='')

    if result[0][2] == 2:
        for h in range(M):
            print(s[result[0][1] + h][result[0][0]], end='')
        print()
    else:
        for h in range(M):
            print(s[result[0][0]][result[0][1] + h], end='')
        print()
