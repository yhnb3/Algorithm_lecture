N = int(input())
s = [[' '] * N for i in range(N)]


def make_star(n, a, b):
    if n == 3:
        for i in range(n):
            for j in range(n):
                if (i % n) // (n // 3) == 1 and (j % n) // (n // 3) == 1:
                    pass
                else:
                    s[i + a][j + b] = '*'
    else:
        make_star(n // 3, a, b)
        make_star(n // 3, a + n // 3, b)
        make_star(n // 3, a + (n // 3) * 2, b)
        make_star(n // 3, a, b + n // 3)
        make_star(n // 3, a + (n // 3) * 2, b + n // 3)
        make_star(n // 3, a, b + (n // 3) * 2)
        make_star(n // 3, a + n // 3, b + (n // 3) * 2)
        make_star(n // 3, a + (n // 3) * 2, b + (n // 3) * 2)


make_star(N, 0, 0)
for i in range(N):
    for j in range(N):
        print(s[i][j], end='')
    print()
