T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    s = [i for i in range(N + 1)]
    pars = [[i] for i in range(N + 1)]
    print('#{} '.format(tc), end="")
    for i in range(M):
        a, b, c = map(int, input().split())
        if b > c:
            b, c = c, b
        if not a:
            for j in pars[s[c]]:
                if j not in pars[s[b]]:
                    pars[s[b]].append(j)
                s[j] = s[b]
        else:
            if s[b] == s[c]:
                print(1, end="")
            else:
                print(0, end="")
    print()

