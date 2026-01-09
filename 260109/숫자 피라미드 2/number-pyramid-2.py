N = int(input())
cnt = 1

for n in range(1,N+1):
    answer = []
    for _ in range(n):
        answer.append(cnt)
        cnt += 1
    for ans in answer:
        print(ans,end=' ')
    print()
