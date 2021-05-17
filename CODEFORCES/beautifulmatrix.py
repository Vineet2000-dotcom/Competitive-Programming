mat = []
for i in range(5):
    list1 = list(map(int, input().split()))
    mat.append(list1)
    
for i in range(5):
    for j in range(5):
        if(mat[i][j] == 1):
            row = i
            column = j
            
print(abs(row-2)+abs(column-2))
