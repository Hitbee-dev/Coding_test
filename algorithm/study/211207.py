V = {0, 1, 2, 3, 4}
L = {0: [1, 2], 1: [2, 3], 2: [3, 4], 3: [4], 4: []}

def dfs(v):
    visited.add(v) # 방문한 곳 표시
    print(v)
    for w in L[v]:
        if w not in visited: # 방문을 안한 곳이라면
            print(v, '->', w)
            dfs(w) # 들어가보자
visited = set()
print(dfs(0))