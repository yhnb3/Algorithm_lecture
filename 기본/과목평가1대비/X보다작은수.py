N, X = map(int, input().split())
input_string = list(map(int, input().split()))
result_string = ''

for i in range(N):
    if input_string[i] < X:
        result_string = result_string + str(input_string[i]) + ' '

print(result_string[:-1])

