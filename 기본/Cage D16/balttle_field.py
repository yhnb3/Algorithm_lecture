import sys
sys.stdin = open('battle_field.txt')

T = int(input())
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    field = [list(input()) for i in range(H)]
    N = int(input())
    move = input()
    tank = ['^', 'v', '<', '>']
    x, y = 0, 0
    for i in range(H):
        for j in range(W):
            if field[i][j] in tank:
                x, y = i, j
                break
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    g = ['U', 'D', 'L', 'R']
    for i in move:
        if i in g:
            dd = g.index(i)
            while 1:
                tx, ty = x + delta[dd][0], y + delta[dd][1]
                if 0 <= tx < H and 0 <= ty < W:
                    if field[tx][ty] == '.':
                        field[x][y] = '.'
                        field[tx][ty] = tank[dd]
                        x, y = tx, ty
                        break
                    else:
                        field[x][y] = tank[dd]
                        break
                else:
                    field[x][y] = tank[dd]
                    break
        else:
            ss = tank.index(field[x][y])
            px, py = x, y
            while 1:
                tx, ty = px + delta[ss][0], py + delta[ss][1]
                if 0 <= tx < H and 0 <= ty < W:
                    if field[tx][ty] == '*':
                        field[tx][ty] = '.'
                        break
                    elif field[tx][ty] == '#':
                        break
                    else:
                        px, py = tx, ty
                else:
                    break

    print('#{} '.format(test_case), end='')
    for i in range(H):
        for j in range(W):
            print('{}'.format(field[i][j]), end='')
        print()




