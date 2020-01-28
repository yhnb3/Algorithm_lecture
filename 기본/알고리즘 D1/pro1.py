import sys
sys.stdin = open("test.txt","r")
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    count = 0
    for i in range(2, N-2):
        for j in range(data[i], -1, -1):
            if j > data[i-1] and j > data[i-2] and j > data[i+1] and j > data[i+2]:
                count += 1
            else:
                break
    print('#{} {}'.format(test_case, count))