N = int(input())
S = [[int(x) for x in input()] for i in range(N)]


def quad_tree(x1, y1, x2, y2):
    flag1 = 0
    flag0 = 0

    if x1 == x2 and y1 == y2:
        print(S[x1][y1], end='')
        return

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if S[i][j]:
                flag0 += 1
            else:
                flag1 += 1
    if not flag0:
        print('0', end='')
        return
    elif not flag1:
        print('1', end='')
        return
    else:
        print('(', end='')
        quad_tree(x1, y1,  x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2)
        quad_tree(x1,  y1 + (y2 - y1) // 2 + 1, x1 + (x2 - x1) // 2, y2)
        quad_tree(x1 + (x2 - x1) // 2 + 1, y1, x2, y1 + (y2 - y1) // 2)
        quad_tree(x1 + (x2 - x1) // 2 + 1, y1 + (y2 - y1) // 2 + 1, x2, y2)
    print(')', end='')


quad_tree(0, 0, N - 1, N - 1)
