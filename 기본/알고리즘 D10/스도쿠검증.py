import sys
sys.stdin = open('스도쿠검증.txt')

T = int(input())

for test_case in range(1, T + 1):

    s = [list(map(int, input().split())) for i in range(9)]

    count = 0

    for i in range(9):
        count1 = [0] * 10
        count2 = [0] * 10
        for j in range(9):
            if count1[s[i][j]] == 1:
                count += 1
                break
            count1[s[i][j]] += 1

            if count2[s[j][i]] == 1:
                count += 1
                break
            count2[s[j][i]] += 1

    for i in range(0, 7, 3):
        for h in range(0, 7, 3):
            count3 = [0] * 10
            for j in range(3):
                for k in range(3):
                    if count3[s[i + j][h + k]] == 1:
                        count += 1
                        break
                    count3[s[i + j][h + k]] += 1

    if count > 0:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, 1))
