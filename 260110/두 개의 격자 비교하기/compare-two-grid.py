n, m = map(int,input().split())

arr_1=[]
arr_2=[]

for _ in range(n):
    raw_data = list(map(int, input().split()))
    arr_1.append(raw_data)

for _ in range(m):
    raw_data = list(map(int, input().split()))
    arr_2.append(raw_data)

for i in range(n):
    for j in range(m):
        a = 0
        if arr_1[i][j] == arr_2[i][j]:
            a = 0
        else:
            a = 1
        print(a,end=' ')
    print()