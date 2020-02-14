import sys
sys.stdin = open('다솔이의다이아몬드.txt')

T = int(input())

for test_case in range(1, T + 1):
    s = input()
    if len(s) == 1:
        print('..#..')
        print('.#.#.')
        print('#.{}.#'.format(s[0]))
        print('.#.#.')
        print('..#..')
    else:
        for j in range(len(s)):
            print('..#.', end='')
        print('.')

        for j in range(len(s)):
            print('.#.#', end='')
        print('.')
        for j in range(len(s)):
            print('#.{}.'.format(s[j]), end='')
        print('#')
        for j in range(len(s)):
            print('.#.#', end='')
        print('.')
        for j in range(len(s)):
            print('..#.', end='')
        print('.')







