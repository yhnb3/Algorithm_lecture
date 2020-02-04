import time

start = time.time()  # 시작 시간 저장

N, K = map(int, input().split())
s = []
for i in range(N):
    a = input()
    s.append(a)

# N = 1
# K = 12
# s = []
# s.append('antaqwetyutica')




alphabet = 'abcdefghijklmnopqrstuvwxyz'
check_box = [0] * 26

for i in s:
    for j in range(len(i)):
        check_box[alphabet.index(i[j])] += 1

test_string = ''

for i in range(26):
    if check_box[i] > 0:
        test_string += alphabet[i]

check_box_box = []
count = 0
for i in range(1 << len(test_string)):
    check_check_box = [0] * len(test_string)
    for j in range(len(test_string)):
        if i & (1 << j):
            check_check_box[j] += 1
            count += 1
    if count == K:
        check_box_box.append(check_check_box)
        break

string_box = []
for i in check_box_box:
    result_string = ''
    for j in range(len(i)):
        if i[j] > 0:
            result_string += test_string[j]
    string_box.append(result_string)

max_num = 0

for i in string_box:
    num_num = 0
    for j in s:
        count = 0
        for h in range(len(j)):
            if j[h] in i:
                count += 1
        if count == len(j):
            num_num += 1
    if max_num < num_num:
        max_num = num_num

if len(test_string) <= K:
    print(len(s))
else:
    print(max_num)



print("time :", time.time() - start)