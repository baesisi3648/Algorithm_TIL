N = int(input())

for n in range(1,N+1):
    for i in range(2*n-1):
        print('*', end='')
    for j in range(N-n):
        print(' ', end='')
    print()