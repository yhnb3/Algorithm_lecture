def f(x):
    if road[x][0]:
        f(road[x][0])
    print('{}'.format(string[x]), end='')
    if road[x][1]:
        f(road[x][1])


T = 10
for tc in range(1, T + 1):
    N = int(input())
    road = [[0] * 2 for i in range(N + 1)]
    string = [0] * (N + 1)
    visit = [0] * (N + 1)
    for i in range(N):
        a_list = list(map(str, input().split()))
        string[int(a_list[0])] = a_list[1]
        for j in range(len(a_list[2:])):
            road[int(a_list[0])][j] = int(a_list[2 + j])
    print('#{} '.format(tc), end='')
    f(1)
    print()






