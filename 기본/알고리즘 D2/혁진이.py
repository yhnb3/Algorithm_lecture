import sys
import random
sys.stdin = open('혁진이.txt')

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    l_h = [[0 for i in range(b)] for j in range(a)]
    l_h[0] = input()
    l_h[1] = input()
    i = 0
    j = 0
    i_move = 0
    j_move = 1
    mem = 0
    ran = ''
    count = 0

    while mem != '@':


        if l_h[i][j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            mem = int(l_h[i][j])
            i += i_move
            j += j_move
        elif l_h[i][j] == '<':
            j_move = -1
            i_move = 0
            i += i_move
            j += j_move
        elif l_h[i][j] == '>':
            j_move = 1
            i_move = 0
            j += j_move
            i += i_move
        elif l_h[i][j] == '^':
            i_move = -1
            j_move = 0
            j += j_move
            i += i_move
        elif l_h[i][j] == 'v':
            i_move = 1
            j_move = 0
            j += j_move
            i += i_move
        elif l_h[i][j] == '_':
            if mem == 0:
                j_move = 1
                i_move = 0
                j += j_move
                i += i_move
            else:
                j_move = -1
                i_move = 0
                i += i_move
                j += j_move
        elif l_h[i][j] == '|':
            if mem == 0:
                j_move = 0
                i_move = 1
                j += j_move
                i += i_move
            else:
                j_move = 0
                i_move = -1
                i += i_move
                j += j_move
        elif l_h[i][j] == '?':
            ran = random.choice(['>', '<', '^', 'v'])
            if ran == '<':
                j_move = -1
                i_move = 0
                i += i_move
                j += j_move
            elif ran == '>':
                j_move = 1
                i_move = 0
                j += j_move
                i += i_move
            elif ran == '^':
                i_move = -1
                j_move = 0
                j += j_move
                i += i_move
            elif ran == 'v':
                i_move = 1
                j_move = 0
                j += j_move
                i += i_move
        elif l_h[i][j] == '@':
            mem = '@'
            j += j_move
            i += i_move
        elif l_h[i][j] == '+':
            mem += 1
            if mem == 16:
                mem = 0
            j += j_move
            i += i_move
        elif l_h[i][j] == '-':
            mem -= 1
            if mem == -1:
                mem = 15
            j += j_move
            i += i_move
        else:
            j += j_move
            i += i_move
        if j == -1:
            j = b-1
        elif j == b:
            j = 0
        if i == -1:
            i = a-1
        elif i == a:
            i = 0
        if count > 100:
            print('NO')
            break
        count += 1
    else:
        print('YES')



