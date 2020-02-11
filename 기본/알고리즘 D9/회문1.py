import sys
sys.stdin = open('회문1.txt')

T = 10

for test_case in range(1, T + 1):
    f_len = int(input())
    s = [list(input()) for i in range(8)]

    count = 0
    for k in range(8):
        for i in range(8 - f_len + 1):
            flag = True
            for h in range(f_len // 2):
                if s[k][h + i] == s[k][-(8 - f_len + 1 - i) - h]:
                    pass
                else:
                    flag = False
                    break

            if flag:
                count += 1

            flag = True
            for o in range(f_len // 2):
                if s[o + i][k] == s[-(8 - f_len + 1 - i) - o][k]:
                    pass
                else:
                    flag = False
                    break
            if flag:
                count += 1

    print('#{} {}'.format(test_case, count))