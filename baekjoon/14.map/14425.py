# N_CNT, M_CNT = 5, 11
# N_CNT, M_CNT = map(int, input().split())
# DATA = [
#     "baekjoononlinejudge",
#     "startlink",
#     "codeplus",
#     "sundaycoding",
#     "codingsh",
#     "baekjoon",
#     "codeplus",
#     "codeminus",
#     "startlink",
#     "starlink",
#     "sundaycoding",
#     "codingsh",
#     "codinghs",
#     "sondaycoding",
#     "startrink",
#     "icerink"]

N_CNT, M_CNT = map(int, input().split())
RESULT = set()
cnt = 0

for _ in range(N_CNT):
    RESULT.add(input())
for _ in range(M_CNT):
    if input() in RESULT:
        cnt += 1
print(cnt)