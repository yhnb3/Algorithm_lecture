dx_j = [1, 0, -1, 0] 	# ->, v, <-, ^ 방향순
dy_i = [0, 1, 0, -1]

Array = [ [9,20,2,18,11], [19,1,25,3,21], [8,24,10,17,7], [15,4,16,5,6], [12,13,22,23,14] ]
IdxTbl = []     # (index1,index2) - key포함X

N = len(Array)
N2 = N*N
for w0 in range(N//2+1):
    i = j = w0
    if N-2*w0-1 == 0:
        IdxTbl.append((i, j))
        continue
    for d in range(4):
        for _ in range(N-2*w0-1):
            IdxTbl.append((i, j))
            ni = i + dy_i[d]
            nj = j + dx_j[d]
            i, j = ni, nj

print(IdxTbl)

# print Array Thr. IdxTbl
for i in range(N2) :
    print(Array[IdxTbl[i][0]][IdxTbl[i][1]], end=" ")
print()

# Sort Array Thr. IdxTbl
for i in range(N2-1) :
    min = i
    for j in range(i+1,N2) :
        if Array[IdxTbl[min][0]][IdxTbl[min][1]] > Array[IdxTbl[j][0]][IdxTbl[j][1]] : min = j              # val값(key) 기준
    idx_i0 = IdxTbl[i][0];      idx_i1 = IdxTbl[i][1]
    min_i0 = IdxTbl[min][0];    min_i1 = IdxTbl[min][1]
    Array[min_i0][min_i1], Array[idx_i0][idx_i1] = Array[idx_i0][idx_i1], Array[min_i0][min_i1]

# print Array Thr. IdxTbl
for i in range(N2) :
    print(Array[IdxTbl[i][0]][IdxTbl[i][1]], end=" ")
print()

for i in range(N) :
    print(Array[i])