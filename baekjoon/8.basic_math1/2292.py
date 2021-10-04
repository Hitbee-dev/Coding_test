n = int(input())
result = 1
cnt = 0
while result < n:
    cnt += 1
    result += (6*cnt)

print(cnt+1)