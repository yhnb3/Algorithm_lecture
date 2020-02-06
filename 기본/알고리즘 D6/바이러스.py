import sys
sys.stdin = open('바이러스.txt')

num = int(input())
S = int(input())
visited = [0]*(num+1)

def v_search(a):
    if visited[a] == 0:
        visited[a] += 1
    for i in range(num+1):
        if ss[a][i] == 1 or ss[i][a] == 1:
            if visited[i] == 0:
                v_search(i)

computer = [list(map(int, input().split())) for i in range(S)]
ss = [[0]*(num+1) for i in range(num+1)]

for i in computer:
    ss[i[0]][i[1]] = 1

v_search(1)

print(sum(visited)-1)





