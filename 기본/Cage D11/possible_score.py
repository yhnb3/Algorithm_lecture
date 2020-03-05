import sys
sys.stdin = open('score.txt')
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    S = list(map(int, input().split()))
    result = []
    # dfs(0, 0)
    check = [0] * 10001
    check[0] = 1
    count = 1
    stackk = [0]
    for j in range(N):
        for i in range(len(stackk)):
            if check[stackk[i] + S[j]] == 0:
                check[stackk[i] + S[j]] = 1
                stackk.append(stackk[i] + S[j])
                count += 1
    print('#{} {}'.format(test_case, count))
