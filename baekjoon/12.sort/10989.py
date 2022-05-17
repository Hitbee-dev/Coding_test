#정렬이지만, 정렬이 아닌 다른방향으로도 문제를 풀 수 있다는 것을 알게 됨..

import sys

N = int(sys.stdin.readline())
arr = [0] * 10001
for _ in range(N):
    M = int(sys.stdin.readline())
    arr[M] = arr[M]+1

for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)