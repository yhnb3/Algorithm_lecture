# import time
#
# time_start = time.time()

N = int(input())

s = [[-1] * (N + 2) for i in range(N + 2)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        s[i][j] = 0

col = [-1] * (N + 1)
result = [0]


def ymq(x, n):
    if x > n:
        result[0] += 1
        return

    for j in range(1, n + 1):
        for k in range(1, x):
            col[x] = j
            if col[k] == col[x]:
                break

            if abs(col[x] - col[k]) == abs(x - k):
                break

        else:
            col[x] = j
            ymq(x + 1, N)
            col[x] = 0

ymq(1, N)

print(result[0])

# print(abs(time_start - time.time()))



