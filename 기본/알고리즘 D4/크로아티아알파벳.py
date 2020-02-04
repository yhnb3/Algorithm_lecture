s = input()
# s = 'dz'

count = 0
i = 0
while i < len(s):
    if s[i] not in 'cdlzns' or i == len(s) - 1:
        count += 1
        i += 1
    else:
        if s[i] == 'c':
            if s[i+1] == '=' or s[i+1] == '-':
                count += 1
                i += 2
            else:
                count += 1
                i += 1
        elif s[i] == 'd':
            if s[i+1] == '-':
                count += 1
                i += 2
            elif s[i+1] == 'z':
                if i == len(s) - 2:
                    count += 2
                    i += 2
                elif s[i+2] == '=':
                    count += 1
                    i += 3
                else:
                    count += 2
                    i += 2
            else:
                count += 1
                i += 1
        elif s[i] == 'l':
            if s[i+1] =='j':
                count += 1
                i += 2
            else:
                count += 1
                i += 1
        elif s[i] == 'n':
            if s[i+1] =='j':
                count += 1
                i += 2
            else:
                count += 1
                i += 1

        elif s[i] == 's':
            if s[i+1] =='=':
                count += 1
                i += 2
            else:
                count += 1
                i += 1

        elif s[i] == 'z':
            if s[i+1] == '=':
                count += 1
                i += 2
            else:
                count += 1
                i += 1
print(count)