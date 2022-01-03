import math

m = int(input())
n = int(input())
buffer = []
for i in range(m, n+1):
    if(i <= 1):
        continue
    check = True
    for p in range(2, int(math.sqrt(i))+1):
        if(i % p == 0):
            check = False
            break
    if(check):
        buffer.append(i)
if(len(buffer) == 0):
    print(-1)
else:
    print(sum(buffer))
    print(min(buffer))
# print(buffer)
