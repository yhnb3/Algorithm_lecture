s = [list(map(int, input().split())) for i in range(9)]
blank_list = []


for i in range(9):
    for j in range(9):
        if s[i][j] == 0:
            blank_list.append([i, j])

def sdoku(b):
    if b == len(blank_list):
        return 1

    x, y = blank_list[b]
    for i in range(1, 10):
        if is_sdoku(x, y, i):
            s[x][y] = i
            if sdoku(b + 1):
                return 1
            s[x][y] = 0

def is_sdoku(a, b, k):
    if k in s[a]:
        return False

    for i in range(9):
        if k == s[i][b]:
            return False

    for i in range(3):
        for j in range(3):
            if k == s[(a//3) * 3 + i][(b//3) * 3 + j]:
                return False

    return True



sdoku(0)

for i in range(9):
    for j in range(9):
        print(s[i][j], end=' ')
    print()


