# Test Case
clothes = [
        [
            ["yellowhat", "headgear"],
            ["redwhat", "headgear"],
            ["greenwhat", "headgear"],
            ["bluewhat", "headgear"],
            ["bluesunglasses", "eyewear"],
            ["bluesunlasses", "eyewear"],
            ["green_turban", "cloth"],
            ["red_turban", "cloth"],
        ],
        [
            ["yellowhat", "headgear"],
            ["bluesunglasses", "eyewear"],
            ["green_turban", "headgear"]
        ],
        [
            ["crowmask", "face"],
            ["bluesunglasses", "face"],
            ["smoky_makeup", "face"]
        ]
    ]

# 1번째 풀이방법 (맞긴 한데 테스트케이스 1번 시간초과뜸)
# from itertools import combinations

# def solution(clothes):
#     dic = {}
#     result = 0
#     for list in clothes:
#         if list[1] not in dic:
#             dic[list[1]] = 1
#         else:
#             dic[list[1]] += 1

#     for i in range(len(dic)):
#         for j in combinations(dic.values(), i+1):
#             if len(j) == 1:
#                 result += j[0]
#             else:
#                 buffer = j[0]
#                 for k in range(1, len(j)):
#                     buffer *= j[k]
#                 result += buffer
            
#             return result
#             # print(result, j)

# 2번째 풀이방법 (정답)
# 각 옷의 종류당 +1을 하고, 옷의 종류를 모두 곱한 후 마지막에 1을 빼준다.
# 이유는 옷을 고르지 않을 경우의 수를 더하기위해 +1을 해주고,
# 1을 빼주는 이유는 모든 옷을 고르지 않을 때 이기 때문이다.
# def multiply(arr):
#     return eval('*'.join(map(str, arr)))

# def solution(clothes):
#     dic = {}
#     arr = []
#     for list in clothes:
#         if list[1] not in dic:
#             dic[list[1]] = 1
#         else:
#             dic[list[1]] += 1

#     for i in dic.values(): # 옷의 종류 당 +1 씩 추가(안입는 경우)
#         arr.append(i+1)
    
#     return multiply(arr) - 1 # 모두 다 안입는 경우를 빼주기위해 -1
#     # print(multiply(arr) - 1)

# 3번째 풀이방법 (정답) (코드 간결화)
def multiply(arr):
    return eval('*'.join(map(str, arr)))

def solution(clothes):
    arr = {}
    for _, v in clothes:
        if v not in arr:
            arr[v] = 2
        elif v in arr:
            arr[v] += 1
    return multiply(arr.values()) - 1
    # print(multiply(arr.values()) - 1)

# 경수 풀이방법
# from collections import Counter
# from functools import reduce
# def solution(clothes):
#     counter = Counter(list(map(lambda x: x[1], clothes)))
#     return reduce(lambda x, y: x * y, [_ + 1 for _ in counter.values()]) - 1
#     # print(reduce(lambda x, y: x * y, [_ + 1 for _ in counter.values()]) - 1)
    

for i in clothes:
    solution(i)