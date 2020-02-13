s = [list(map(int, input().split())) for i in range(9)]
blank_list = []


for i in range(9):
    for j in range(9):
        if s[i][j] == 0:
            blank_list.append([i, j])

def sdoku(b):
    if b == len(blank_list):
        if is_sdoku(b-1):
            return 1

    for i in range(1, 10):
        s[blank_list[b][0]][blank_list[b][1]] = i
        if sdoku(b + 1):
            return 1



def is_sdoku(a, o):
    for k in range(10):
        if k != blank_list[a][0]:
            if s[k][blank_list[a][1]] == o:
                return False

    for k in range(10):
        if k != blank_list[a][1]:
            if s[blank_list[a][0]][k] == o:
                return False

    for i in range(3):
        if i != blank_list[a][0]:
            for j in range(3):
                if j != blank_list[a][1]:
                    if o == s[i][j]:
                        return False

    return True


sdoku(0)

for i in range(9):
    for j in range(9):
        print(s[i][j], end=' ')
    print()


