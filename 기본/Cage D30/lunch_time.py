import collections


def down_stair():
    max_num = 0
    st1 = sorted(stair1)
    st2 = sorted(stair2)
    s1_len = 0
    s2_len = 0
    s1 = -1
    s2 = -1
    if stair1:
        s1 = st1[0]
        s1_len = len(st1)
    if stair2:
        s2 = st2[0]
        s2_len = len(st2)
    while s1_len > 0 or s2_len > 0:
        if max_num >= min_num:
            stair13.clear()
            stair23.clear()
            return max_num
        if s1_len > 0:
            i = 0
            while i < len(stair13):
                stair13[i][1] += 1
                if stair13[i][1] == stair[0][2]:
                    z, t = stair13.popleft()
                    max_num = max(z + 1 + stair[0][2], max_num)
                    s1_len -= 1
                    continue
                i += 1
            for i in range(len(st1)):
                if st1[i] == s1:
                    if len(stair13) < 3:
                        stair13.append([st1[i], 0])
                    else:
                        st1[i] += 1
            s1 += 1
        if s2_len > 0:
            j = 0
            while j < len(stair23):
                stair23[j][1] += 1
                if stair23[j][1] == stair[1][2]:
                    z, t = stair23.popleft()
                    max_num = max(z + 1 + stair[1][2], max_num)
                    s2_len -= 1
                    continue
                j += 1
            for k in range(len(st2)):
                if st2[k] == s2:
                    if len(stair23) < 3:
                        stair23.append([st2[k], 0])
                    else:
                        st2[k] += 1
            s2 += 1
    return max_num


def cb(c, s):
    global min_num
    if s == 1:
        stair1.append(abs(stair[s - 1][0] - people[c][0]) + abs(stair[s - 1][1] - people[c][1]))
    else:
        stair2.append(abs(stair[s - 1][0] - people[c][0]) + abs(stair[s - 1][1] - people[c][1]))
    if c == p_num - 1:
        min_num = min(down_stair(), min_num)
        return
    cb(c + 1, 1)
    stair1.pop()
    cb(c + 1, 2)
    stair2.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [[0] * N for i in range(N)]
    stair = []
    people = []
    stair1 = []
    stair2 = []
    stair13 = collections.deque()
    stair23 = collections.deque()
    min_num = float('INF')
    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(N):
            room[i][j] = a[j]
            if a[j] == 1:
                people.append([i, j])
            elif a[j] != 0:
                stair.append([i, j, a[j]])
    p_num = len(people)
    cb(0, 1)
    stair1.pop()
    cb(0, 2)
    print('#{} {}'.format(tc, min_num))
