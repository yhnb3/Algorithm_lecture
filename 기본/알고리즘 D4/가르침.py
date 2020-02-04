N, K = map(int, input().split())
s = []
for i in range(N):
    a = input()
    a = a.replace('a', '')
    a = a.replace('c', '')
    a = a.replace('i', '')
    a = a.replace('n', '')
    a = a.replace('t', '')
    s.append(a)


# N = 3
# K = 6
# s = []
# s.append('antarctica')
# s.append('antahellotica')
# s.append('antacartica')

alphabet = 'bdefghjklmopqrsuvwxyz'
rep = 'acnti'
check_box = [0]*21
len(alphabet)
for i in s:
    for j in range(len(i)):
        check_box[alphabet.index(i[j])] += 1

test_string = ''



for i in range(21):
    if check_box[i] > 0:
        test_string += alphabet[i]
check_box_box = []

for i in range(1 << len(test_string)): # 2^21
    count = 0
    check_check_box = [0] * len(test_string)
    for j in range(len(test_string)): # 21
        if i & (1 << j):
            check_check_box[j] += 1
            count += 1
    if count == K-5:
        check_box_box.append(check_check_box)



string_box = []
for i in check_box_box: #21
    result_string = ''
    for j in range(len(i)):# 21
        if i[j] > 0:
            result_string += test_string[j]
    string_box.append(result_string)

max_num = 0

for i in string_box: #
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

if len(test_string+rep) <= K:
    print(len(s))
else:
    print(max_num)




