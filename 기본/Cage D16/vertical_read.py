import sys
sys.stdin = open('vertical_read.txt')

T = int(input())
for test_case in range(1, T + 1):
    s = [[-1] * 15 for i in range(5)]
    sum_num = 0
    for i in range(5):
        a = input()
        for j in range(len(a)):
            s[i][j] = a[j]
            sum_num += 1
    flag = True
    print('#{} '.format(test_case), end='')
    for i in range(15):
        for j in range(5):
            if sum_num == 0:
                flag = False
                break
            if s[j][i] != -1:
                print('{}'.format(s[j][i]), end='')
                sum_num -= 1
        if not flag:
            break
    print()


