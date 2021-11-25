# 산술평균: N개의 수들의 합을 N으로 나눈 값
# 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값: N개의 수들 중 가장 많이 나타나는 값(단, 같은값이 여러개라면 가장 작은 값 중에 두번째 값 출력)
# 범위: N개의 수들 중 최댓값과 최솟값의 차이

from collections import Counter
import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(arr) / N))

# 중앙값
arr.sort()
print(arr[int(N / 2)])

# 최빈값
nums_s = Counter(arr).most_common()
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])

# 범위
print(max(arr)-min(arr))
