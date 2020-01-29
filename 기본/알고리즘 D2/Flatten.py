import sys
sys.stdin = open ('Flatten.txt')

T = 10
for test_case in range(1, T + 1):
    num = int(input())
    boxes = list(map(int, input().split()))
    for i in range(num):
        max_num = 0
        max_idx = 0
        min_num = 101
        min_idx = 0

        for j in range(len(boxes)):

            if boxes[j] > max_num:
                max_num = boxes[j]
                max_idx = j
            if boxes[j] < min_num:
                min_num = boxes[j]
                min_idx = j
        else:
            if boxes[max_idx] - boxes[min_idx] <= 1:
                break
            boxes[max_idx] -= 1
            boxes[min_idx] += 1

    max_num = 0
    min_num = 101
    for i in range(len(boxes)):
        if boxes[i] > max_num:
            max_num = boxes[i]
            max_idx = i

        if boxes[i] < min_num:
            min_num = boxes[i]
            min_idx = i

    print('#{} {}'.format(test_case, max_num - min_num))