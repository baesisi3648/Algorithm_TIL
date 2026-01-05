N = int(input())

for n in range(N):
    a, b = map(int,input().split())
    total = 0
    for c in range(a, b+1):
        if c % 2 ==0:
            total += c
    print(total)