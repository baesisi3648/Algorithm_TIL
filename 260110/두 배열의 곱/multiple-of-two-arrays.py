matrix1=[]
matrix2=[]

for _ in range(4):
    row_data = list(map(int,input().split()))
    matrix1.append(row_data)

for _ in range(3):
    row_data = list(map(int,input().split()))
    matrix2.append(row_data)


for i in range(3):
    for j in range(3):
        print(matrix1[i][j] * matrix2[i][j],end=' ')
    print()