def my_sqrt(X):
    gab = 1
    a = X+1
    b = 1
    while gab > 0.00000000001:
        if ((a+b)/2)**2 > X:
            a = (a+b)/2
            gab = a**2 - X
        else:
            b = (a+b)/2
            gab = X - b**2
    return a

print(my_sqrt(2))








