N = int(input())

room = [[1] * (N + 2) for i in range(N + 2)]
for i in range(1, N + 1):
    a = list(map(int, input().split()))
    for j in range(1, N + 1):
        room[i][j] = a[j - 1]

