import sys
sys.stdin = open('find_road.txt')
import collections

T = 10
for test_case in range(1, T + 1):
    N, num = map(int, input().split())
    r = [[] for i in range(100)]
    input_data = list(map(int, input().split()))
    for i in range(0, num * 2, 2):
        r[input_data[i]].append(input_data[i + 1])
    que = collections.deque()
    que.append(0)
    visit = [0] * 100
    while que:
        x = que.popleft()
        visit[x] = 1
        if x == 99:
            print('#{} {}'.format(N, 1))
            break
        if r[x]:
            for z in r[x]:
                if visit[z] == 0:
                    que.append(z)
    else:
        print('#{} {}'.format(N, 0))




