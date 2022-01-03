N = int(input())
arr = []
for _ in range(N):
    M = int(input())
    arr.append(M)
arr.sort()

for i in arr:
    print(i)