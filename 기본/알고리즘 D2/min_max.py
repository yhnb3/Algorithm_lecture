import sys
sys.stdin = open("min_max.txt", "r")
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    a = int(input())
    b = input().split(" ")
    print('#{} '.format(test_case), end="")

    for i in range(0, a-1) :
        if int(b[i]) > int(b[i+1]):
            b[i], b[i+1] = b[i+1], b[i]
    max_num = int(b[a-1])

    for i in range(-1, -a, -1):
        if int(b[i]) < int(b[i-1]):
            b[i], b[i-1] = b[i-1], b[i]
    min_num = int(b[0])

    print(max_num - min_num)
