import sys
input = sys.stdin.readline

# 값 받아오기
N = int(input().strip())
datas = list(map(int, input().split()))

# -1로 채워진 배열 미리 생성
answer = [-1 for _ in range(N)]

# 인덱스를 저장할 스택 선언
stack = []

# 모든 수 앞에서부터 시작
for i in range(N):
    # 만약 현재값이 stack 최상단에 있는 값보다 크거나, 비어있지 않다면
    while stack != [] and datas[i] > datas[stack[-1]]:
        # 전부 answer[idx]에 반영하면서 pop
        answer[stack.pop()] = datas[i]
    # 스택이 비어있거나, 현재값이 stack 최상단에 있는 값보다 작다면 push
    stack.append(i)
print(*answer)


# solution list #1
# datas = list(map(int, input().split()))
# for idx, data in enumerate(datas):
#     if idx+1 == N:
#         print(-1, end=' ')
#         break
#     for i in range(idx+1, N):
#         if data < datas[i]:
#             print(datas[i], end=' ')
#             break
#         if i+1 == N:
#             print(-1, end =' ')

# solution dictionary #2
# datas = {k: v for k, v in enumerate(map(int, input().split()))}
# for idx, v in datas.items():
#     if idx+1 == N:
#         print(-1, end =' ')
#         break
#     for i in range(idx+1, N):
#         if v < datas[i]:
#             print(datas[i], end=' ')
#             break
#         if i+1 == N:
#             print(-1, end =' ')

# solution deque #3
# datas = deque(map(int, input().split()))
# for i in range(N):
#     if i+1 == N:
#         print(-1, end=' ')
#         break
#     x = datas.popleft()
#     for idx, data in enumerate(datas):
#         if x < data:
#             print(data, end=' ')
#             break
#         if idx+1 == len(datas):
#             print(-1, end=' ')