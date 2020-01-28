data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
result = 0
maxHeight = 9
for i in range(maxHeight):
    count = 0
    for j in range(i, maxHeight):
        if data[i] > data[j]:
            count += 1
    if result < count:
        result = count
print(result)
