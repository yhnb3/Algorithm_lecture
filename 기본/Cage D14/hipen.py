T = int(input())
for test_case in range(1, T + 1):
    s = input()
    N = int(input())
    l = list(map(int, input().split()))
    cnt = [0] * (len(s) + 1)
    for i in range(N):
        cnt[l[i]] += 1

    print('#{} '.format(test_case), end='')
    for i in range(len(s)):
        for j in range(cnt[i]):
            print('-', end='')
        print('{}'.format(s[i]), end='')
    for j in range(cnt[len(s)]):
        print('-', end='')
    print()




