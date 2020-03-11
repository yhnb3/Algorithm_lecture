import sys
sys.stdin = open('go_back_room.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for i in range(N)]
    S1 = sorted(S)
    check = 0
    count = [0] * N
    temp = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            a = max(S1[i])
            b = min(S1[i])
            if a & 1:
                a = a + 1
            if not (b & 1):
                b = b - 1
            if b <= S1[j][0] <= a or b <= S1[j][1] <= a:
                count[i] += 1
                count[j] += 1
                temp[i][j], temp[j][i] = 1, 1
                check += 1

    in_room = [0] * N
    result = 1
    que = []
    while check > 0:
        max_idx = 0
        max_num = max(count)
        for i in range(N):
            if not in_room[i]:
                if count[i] == max_num:
                    in_room[i] += 1
                    max_idx = i
                    break
        que.clear()
        for i in range(N):
            if not in_room[i]:
                if temp[i][max_idx] or temp[max_idx][i]:
                    temp[i][max_idx], temp[max_idx][i] = 0, 0
                    count[i] -= 1
                    count[max_idx] -= 1
                    check -= 1
                else:
                    if que:
                        for k in que:
                            if temp[i][k] or temp[k][i]:
                                break
                        else:
                            que.append(i)
                            in_room[i] += 1
                    else:
                        que.append(i)
                        in_room[i] += 1
        for j in que:
            for i in range(N):
                if not in_room[i]:
                    if temp[i][j] or temp[j][i]:
                        temp[i][j], temp[j][i] = 0, 0
                        count[i] -= 1
                        count[j] -= 1
                        check -= 1
        result += 1
    print('#{} {}'.format(test_case, result))







