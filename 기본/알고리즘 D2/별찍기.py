# star =[[" " for a in range(81)] for b in range(81)]
# def dot_star(a = 0, b = 0, s = 27):
#
#     if s == 3:
#         for i in range(0+a, s+a):
#             for j in range(0+b, s+b):
#                 if ((i % s)//(s/3) != 1) or ((j % s)//(s/3) != 1):
#                     star[i][j] = "*"
#         return star
#     else:
#         return dot_star(a, b, s//3), dot_star(a+s//3, b, s//3), dot_star(a+(s//3)*2, b, s//3), dot_star(a, b+s//3, s//3), dot_star(a, b+(s//3)*2, s//3), dot_star(a+(s//3)*2, b+s//3, s//3), dot_star(a+(s//3)*2, b+(s//3)*2, s//3), dot_star(a+s//3, b+(s//3)*2, s//3)
#
# dot_star(0, 0, 81)
#
# for i in range(81):
#     for j in range(81):
#         print(star[i][j], end="")
#     print("")


print(3&1)
