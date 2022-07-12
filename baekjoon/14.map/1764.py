# 듣도 보도 못한 사람 = N
# 보도 못한 사람 = M

import sys
input = sys.stdin.readline

N_CNT, M_CNT = map(int, input().split())
N = set()
result = []
for _ in range(N_CNT):
    N.add(input().strip())

for i in range(M_CNT):
    buf = input().strip()
    if buf in N:
        result.append(buf)

print(len(result))
result.sort()
for _ in result:
    print(_)