import sys
sys.stdin = open('미로1.txt')

T = 10

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def maze1(a, b):
    if s[a][b] == 3:
        result.append(1)

    for i in range(4):
        if s[a + dx[i]][b + dy[i]] != 1:
            if visit[a + dx[i]][b + dy[i]] == 0:
                visit[a + dx[i]][b + dy[i]] = 1
                maze1(a + dx[i], b + dy[i])


for test_case in range(1, T + 1):
    result = []
    visit = [[0] * 14 for i in range(14)]
    tc = int(input())
    s = [[int(x) for x in input()] for i in range(16)]

    maze1(1, 1)

    if result:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))