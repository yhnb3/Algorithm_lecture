import sys
sys.setrecursionlimit(10 ** 6)

N, r, c = map(int, input().split())


def z_search(start_x, start_y, end_x, end_y):
    k = 0
    for i in range((N - 1) * 2, 0, -1):
        if not i & 1:
            if r <= start_x + (end_x - start_x) // 2:
                end_x = end_x - (end_x - start_x) // 2 - 1
            else:
                start_x = start_x + (end_x - start_x) // 2 + 1
                k += 2 ** (i + 1)
        else:
            if c <= start_y + (end_y - start_y) // 2:
                end_y = end_y - (end_y - start_y) // 2 - 1
            else:
                start_y = start_y + (end_y - start_y) // 2 + 1
                k += 2 ** (i + 1)

    return start_x, start_y, k


def z_move(x, y, chk):
    if x == r and y == c:
        result[0] = chk
        return 1

    if chk % 4 == 0:
        if z_move(x, y + 1, chk + 1):
            return 1
    elif chk % 4 == 1:
        if z_move(x + 1, y - 1, chk + 1):
            return 1
    elif chk % 4 == 2:
        if z_move(x, y + 1, chk + 1):
            return 1


result = [0]
k = z_search(0, 0, 2 ** N - 1, 2 ** N - 1)
z_move(k[0], k[1], 0)
print(k[2] + result[0])
