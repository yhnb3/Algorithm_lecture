import sys
sys.stdin = open('사다리2.txt')

T = 10

def left_move(i, j):
    if j-1 < 0:
        pass
    else:
        if s[i][j-1] == 1:
            a[1] -= 1
            a[2] += 1
            left_move(i, j-1)

def right_move(i, j):
    if j+1 > 99:
        pass
    else:
        if s[i][j+1] == 1:
            a[1] += 1
            a[2] += 1
            right_move(i, j+1)


for test_case in range(1, T + 1):
    tc = int(input())
    s = [list(map(int, input().split())) for i in range(100)]
    min_num = 12354678918541
    min_idx = 0
    count = 0
    a = [0, 0, 0]
    for i in s:
        i.append(0)

    while count < 100:
        if a[0] == 99:
            if min_num > a[2]:
                min_num = a[2]
                min_idx = count
            a = [0, 0, 0]
            count += 1
            a[1] = count
            continue

        if a[0] == 0:
            if s[a[0]+1][a[1]] == 1:
                a[0] += 1
                a[2] += 1
                continue
            else:
                count += 1
                a[1] = count
                continue

        elif s[a[0]][a[1] + 1] == 1:
            if a[1] + 1 > 99:
                pass
            else:
                right_move(a[0], a[1])
                a[0] += 1
                a[2] += 1
                continue

        elif s[a[0]][a[1] - 1] == 1:
            if a[1] - 1 < 0:
                pass
            else:
                left_move(a[0], a[1])
                a[0] += 1
                a[2] += 1
                continue

        if s[a[0] + 1][a[1]] == 1:
            a[0] += 1
            a[2] += 1
            continue



    print('#{} {}'.format(test_case, min_idx))

