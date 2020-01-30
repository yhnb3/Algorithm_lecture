
def my_sqrt():
    gab = 1
    a = 2
    b = 1
    while gab > 0.000000001:
        if ((a+b)/2)**2 > 2:
            a = (a+b)/2
            gab = a**2 - 2
        else:
            b = (a+b)/2
            gab = 2 - b**2
    return a

print(my_sqrt())








