import sys
sys.stdin = open('두지점경로유무.txt')

T = int(input())

def is_end(a):
    if a == end:
        result[0] += 1

    for i in range(1, V + 1):
        if i in s[a]:
            if visit[i] == 0:
                visit[i] = 1
                is_end(i)
                if result[0]:
                    break

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    s = [[] for i in range(V + 1)]
    visit = [0] * (V + 1)
    result = [0]

    for i in range(E):
        a, b = map(int, input().split())
        s[a].append(b)

    start, end = map(int, input().split())

    visit[start] = 1
    is_end(start)

    print('#{} {}'.format(test_case, result[0]))






