matrix = []
for _ in range(3):
    row_data = list(map(int, input().split()))
    matrix.append(row_data)

for i in range(3):
    for j in range(3):
        print(3*matrix[i][j], end=' ')
    print()


