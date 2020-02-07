import sys
sys.stdin = open('수의새로운연산.txt')

T = int(input())
s = [[0]*400 for i in range(400)]
count = 1
for i in range(2, 400):
    for j in range(1, i):
        s[i-j][j] = count
        count += 1

def idx_search(a, ss):
    for i in range(1, 400):
        for j in range(1, 400):
            if ss[i][j] == a:
                return i, j


for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    result = []
    result.append(idx_search(a, s)[0] + idx_search(b, s)[0])
    result.append(idx_search(a, s)[1] + idx_search(b, s)[1])

    print('#{} {}'.format(test_case, s[result[0]][result[1]]))