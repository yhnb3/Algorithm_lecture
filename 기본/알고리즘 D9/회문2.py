import sys
sys.stdin = open('회문2.txt')

T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    s = [list(input()) for i in range(100)]

    max_len = 0

    for k in range(100):
        for i in range(100):
            for j in range(i + 1, 101):
                flag = True
                for h in range((j-i)//2):
                    if s[k][h + i] == s[k][-(h + 1) - (100 - j)]:
                        pass
                    else:
                        flag = False
                        break
                if flag:
                    if max_len < (j-i):
                        max_len = (j-i)

            for u in range(k + 1, 101):
                flag = True
                for o in range((u-k)//2):
                    if s[o + k][i] == s[-(o + 1) - (100 - u)][i]:
                        pass
                    else:
                        flag = False
                        break
                if flag:
                    if max_len < (u-k):
                        max_len = (u-k)

    print('#{} {}'.format(tc, max_len))
