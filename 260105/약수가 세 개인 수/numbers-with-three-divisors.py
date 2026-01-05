start, end = map(int, input().split())
count = 0

for n in range(start, end+1):
    cnt = 0
    for a in range(1, n+1):
        if n % a  == 0:
            cnt += 1
    if cnt == 3:
        count += 1

print(count)
