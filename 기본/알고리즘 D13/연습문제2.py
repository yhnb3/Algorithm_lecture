import time

start_time = time.time()

N = 10

A = [0] * N
count = 0

def power_set2(n, k, sum_num):
    global count
    if n == k:
        if sum_num == 10:
            count += 1

    else:
        if sum_num + k + 1 <= 10:
            A[k] = 1
            power_set2(n, k + 1, sum_num + k + 1)
        A[k] = 0
        power_set2(n, k + 1, sum_num)

power_set2(N, 0, 0)

print(time.time() - start_time, count)