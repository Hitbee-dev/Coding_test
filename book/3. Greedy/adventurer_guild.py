# 모험가 길드

# 한 마을에 모험가가 N명 있다.
# 모험가 길드에서는 N명의 모험가를 대상으로 "공포도"를 측정했는데, "공포도"가 높은 모험가는 쉽게 공포를 느껴
# 위험상황에서 제대로 대처할 능력이 떨어진다.

# 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한
# 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했다.

# 동빈이는 최대 몇개의 모험가 그룹을 만들 수 있는지 알아내라.
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하시오.

# 예시
# N = 5(모험가의 수)
# 2 3 1 2 2(각 모험가의 공포도)

""" 요약
    가장 공포도가 작은 사람들로 구성하면 된다.
    그룹에 포함 된 인원수를 제거한다.
    단, 마을에 남아있어도 되기 때문에 모든 모험가를 특정한 그룹에 넣을 필요는 없다.
"""

N = int(input())
Array = list(map(int, input().split()))
Array.sort()

# 내가 푼 방법
# def guild(n, arr):
#     cnt = 0
#     check = 0
#     while True:
#         if n < 1 or (n - arr[0]) < 0:
#             break
#         flag = True
#         if arr[0] == 1:
#             cnt += 1
#             n -= 1
#             del arr[0]
#         else:
#             if len(arr) < arr[check]:
#                 break
#             for i in range(arr[check]):
#                 if arr[i] > arr[check]:
#                     flag = False
#             if flag == True:
#                 n -= arr[check]
#                 for _ in range(arr[check]):
#                     del arr[0]
#                 check = 0
#                 cnt += 1
#             else:
#                 check += 1
#                 pass
#     return cnt
# print(guild(N, Array))

# 해답
def guild(arr):
    cnt = 0
    result = 0
    for i in arr:
        cnt += 1
        if cnt >= i:
            result += 1
            cnt = 0
    return result
print(guild(Array))