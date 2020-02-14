import sys
sys.stdin = open('효율적인해킹.txt')

max_len = 0

N, M = map(int, input().split())
s = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    s[b].append(a)

c_c = [0] * (N + 1)

for i in range(1, N + 1):
    if s[i]:
        count = 0
        visit = [0] * (N + 1)
        result = [i]
        visit[i] = 1

        while result:
            k = result.pop()
            count += 1
            for j in s[k]:
                if visit[j] == 0:
                    visit[j] = 1
                    result.append(j)

        c_c[i] = count

max_len = max(c_c)
for i in range(len(c_c)):
    if c_c[i] == max_len:
        print(i, end=' ')
print()







