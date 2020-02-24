N = int(input())

#
def move(x, y, c):
    if x == N and y == N:
        result[0] += 1
        return

    if c == 0:  # 가로로 움직였을때
        if y == N:
            return
        if x == N:
            if room[x][y + 1] == 0:
                move(x, y + 1, 0)
            return

        for i in [0, 2]:
            if i == 2:
                if (room[x + dx[i]][y + dy[i]] == 0 and room[x][y + dy[i]] == 0) and room[x + dx[i]][y] == 0:
                    move(x + dx[i], y + dy[i], i)

            else:
                if room[x + dx[i]][y + dy[i]] == 0:
                    move(x + dx[i], y + dy[i], i)

    elif c == 1:  # 세로로 움직였을때
        if x == N:
            return
        if y == N:
            if room[x + 1][y] == 0:
                move(x + 1, y, 0)
            return

        for i in [1, 2]:
            if i == 2:
                if room[x + dx[i]][y + dy[i]] == 0 and room[x][y + dy[i]] == 0 and room[x + dx[i]][y] == 0:
                    move(x + dx[i], y + dy[i], i)

            else:
                if room[x + dx[i]][y + dy[i]] == 0:
                    move(x + dx[i], y + dy[i], i)

    elif c == 2:  # 대각선으로 움직였을때
        if y == N:
            if room[x + 1][y] == 0:
                move(x + 1, y, 0)
            return

        if x == N:
            if room[x][y + 1] == 0:
                move(x, y + 1, 0)
            return

        if y == N - 1 and x == N - 1:
            if room[x + 1][y + 1] == 0 and room[x][y + 1] == 0 and room[x + 1][y] == 0:
                move(x + 1, y + 1, 2)
            return

        for i in [0, 1, 2]:
            if i == 2:
                if room[x + dx[i]][y + dy[i]] == 0 and room[x][y + dy[i]] == 0 and room[x + dx[i]][y] == 0:
                    move(x + dx[i], y + dy[i], i)

            else:
                if room[x + dx[i]][y + dy[i]] == 0:
                    move(x + dx[i], y + dy[i], i)


room = [[1] * (N + 2) for i in range(N + 2)]
for i in range(1, N + 1):
    a = list(map(int, input().split()))
    for j in range(1, N + 1):
        room[i][j] = a[j - 1]

dx = [0, 1, 1]
dy = [1, 0, 1]
result = [0]
que = [[1, 2, 0]]

# while que:  # BFS로 풀기
#     if room[N][N] == 1 or (room[N][N - 1] == 1 and room[N - 1][N] == 1): # 도착할 수 없는 경우
#         break
#
#     x, y, c = que.pop()
#     if x == N and y == N:
#         result[0] += 1
#
#     elif c == 0:  # 가로로 움직였을때
#         if y == N:
#             continue
#
#         if x == N:
#             if room[x][y + 1] == 0:
#                 que.append([x, y + 1, 0])
#                 continue
#
#         for i in [0, 2]:
#             if i == 2:
#                 if room[x + dx[i]][y + dy[i]] == 0 and room[x][y + dy[i]] == 0 and room[x + dx[i]][y] == 0:
#                     que.append([x + dx[i], y + dy[i], i])
#             else:
#                 if room[x + dx[i]][y + dy[i]] == 0:
#                     que.append([x + dx[i], y + dy[i], i])
#
#     elif c == 1:  # 세로로 움직였을때
#         if x == N:
#             continue
#
#         if y == N:
#             if room[x + 1][y] == 0:
#                 que.append([x + 1, y, 1])
#                 continue
#
#         for i in [1, 2]:
#             if i == 2:
#                 if room[x + dx[i]][y + dy[i]] == 0 and room[x][y + dy[i]] == 0 and room[x + dx[i]][y] == 0:
#                     que.append([x + dx[i], y + dy[i], i])
#
#             else:
#                 if room[x + dx[i]][y + dy[i]] == 0:
#                     que.append([x + dx[i], y + dy[i], i])
#
#     elif c == 2:  # 대각선으로 움직였을때
#         if y == N:
#             if room[x + 1][y] == 0:
#                 que.append([x + 1, y, 1])
#                 continue
#
#         if x == N:
#             if room[x][y + 1] == 0:
#                 que.append([x, y + 1, 0])
#                 continue
#
#         if x == N - 1 and y == N - 1:
#             if room[x + 1][y + 1] == 0:
#                 que.append([x + 1, y + 1, 2])
#                 continue
#
#         for i in [0, 1, 2]:
#             if i == 2:
#                 if room[x + dx[i]][y + dy[i]] == 0 and room[x][y + dy[i]] == 0 and room[x + dx[i]][y] == 0:
#                     que.append([x + dx[i], y + dy[i], i])
#
#             else:
#                 if room[x + dx[i]][y + dy[i]] == 0:
#                     que.append([x + dx[i], y + dy[i], i])

if room[N][N] == 1 or (room[N][N - 1] == 1 and room[N - 1][N] == 1):
    print(result[0])
else:
    move(1, 2, 0)
    print(result[0])