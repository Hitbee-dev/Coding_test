'''
# 문제
교준이는 아래의 세 가지 방법으로 라면을 구매할 수 있다.

1. i번 공장에서 라면을 하나 구매한다(1 ≤ i ≤ N). 이 경우 비용은 3원이 든다.
2. i번 공장과 (i+1)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-1). 이 경우 비용은 5원이 든다.
3. i번 공장과 (i+1)번 공장, (i+2)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-2). 이 경우 비용은 7원이 든다.

# 입력
첫 번째 줄에 라면 공장의 개수를 의미하는 자연수 N가 주어진다.
두번째 줄에 N개의 정수 A1, ···, AN가 사이에 공백을 두고 주어진다.

# 출력
첫 번째 줄에 교준이가 필요한 최소 금액을 출력한다.
'''

import sys
input = sys.stdin.readline

N = int(input().strip())
A = map(int, input().split())
arr = []
buf = []
result = 0
count = 0
flag = 0
for idx, i in enumerate(A):
    count += 1
    buf.append(i)
    if i == 0:
        count = 0
        buf.pop()
        arr.append(buf)
        buf = []
    if i == 0 or count == 3:
        # print(count, arr)

        count = 0
        arr.append(buf)
        buf = []
    elif idx+1 == N:
        arr.append(buf)
# print(arr)
for data in arr:
    if data == []:
        continue
    result += (sum(data)*3)-len(data)+1
print(result)