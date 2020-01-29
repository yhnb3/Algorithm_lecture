star =[[" " for a in range(9)] for b in range(9)]
def dot_star(a=0, b=0, s=9):
    if s == 3:
        for i in range(0, s):
            for j in range(0, s):
                if (i//(s/3) != 1) or (j//(s/3) != 1):
                    star[i+a][j+b] = "*"
        return star
    else:
        return dot_star(0, 0, s//3), dot_star(3, 0, s//3), dot_star(6, 0, s//3), dot_star(0, 3, s//3), dot_star(0, 6, s//3), dot_star(6, 3, s//3), dot_star(6, 6, s//3), dot_star(3, 6, s//3)

dot_star(0, 0, 9)

for i in range(9):
    for j in range(9):
        print(star[i][j], end="")
    print("")