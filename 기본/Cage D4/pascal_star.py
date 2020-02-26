N = int(input())

s = [[' '] * ((N // 3) * 5 + (N // 3) - 1) for i in range(N)]


def pascal_star(n, a, b):
    if n == 3:
        for i in range(3):
            for j in range(5):
                if i == 0 and j == 2:
                    s[i + a][j + b] = '*'
                elif i == 1 and (j == 1 or j == 3):
                    s[i + a][j + b] = '*'
                elif i == 2:
                    s[i + a][j + b] = '*'

    else:
        pascal_star(n//2, a, b + n // 2)
        pascal_star(n//2, a + n // 2, b)
        pascal_star(n//2, a + n // 2, b + n)


pascal_star(N, 0, 0)
for i in range(N):
    print(''.join(s[i]))




