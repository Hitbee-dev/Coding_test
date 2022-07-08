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
DATA = [input() for _ in range(N_CNT+M_CNT)]

cnt = 0
for i in DATA[N_CNT:]:
    if i in set(DATA[:N_CNT]):
        cnt += 1
print(cnt)