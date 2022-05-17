N, M = map(int, input().split())
arr = []

def func(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(idx, N):
        arr.append(i+1)
        func(depth+1, i, N, M)
        arr.pop()

func(0, 0, N, M)