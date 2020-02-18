import sys
sys.stdin = open('미로.txt')

T = int(input())


def maze_runner(x, y):
    if x == end[0] and y == end[1]:
        return 1

    maze[x][y] = 1
    for i in range(4):
        if maze[x + dx[i]][y + dy[i]] != 1:
            if maze_runner(x + dx[i], y + dy[i]):
                return 1


for test_case in range(1, T + 1):
    N = int(input())
    start = []
    end = []
    maze = [[1] * (N + 2) for i in range(N + 2)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(1, N + 1):
        a = [int(x) for x in input()]
        for j in range(1, N + 1):
            maze[i][j] = a[j - 1]
            if maze[i][j] == 2:
                start.append(i)
                start.append(j)

            elif maze[i][j] == 3:
                end.append(i)
                end.append(j)

    if maze_runner(start[0], start[1]):
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))


