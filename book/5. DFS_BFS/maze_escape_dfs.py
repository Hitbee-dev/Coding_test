# 미로 탈출 DFS

""" 요약
    N, M 크기의 직사각형 형태의 미로에 갇혔다.
    (1, 1)부터 시작해서 (N, M)의 출구로 탈출해야하는데,
    괴물이 있는 부분은 0, 없는 부분은 1로 되어있다.
    이때 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라.
    ※ 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
    ※ 4 <= N, M <= 200
"""

# 입력예시  | 출력예시
# 5 6      | 10
# 101010
# 111111
# 000001
# 111111
# 111111

def dfs(x, y, move):
    cnt = move
    if x == N-1 and y == M-1:
        print(cnt)
        return
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return    
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 2
        print("==============================================")
        print(f"현재까지 이동 거리: {cnt}, 현재 위치: {x}, {y}")
        for i in graph:
            print(i)
        dfs(x, y+1, cnt) # 우
        dfs(x+1, y, cnt) # 하
        dfs(x-1, y, cnt) # 상
        dfs(x, y-1, cnt) # 좌
        return

graph = [
    [1, 1, 1, 1, 1, 1], 
    [0, 1, 0, 0, 0, 0], 
    [1, 1, 0, 1, 1, 1], 
    [1, 0, 0, 1, 0, 1], 
    [1, 1, 1, 1, 0, 1]
]
N, M = 5, 6
Move = 1
"""
    graph = []
    N, M = map(int, input().split())
    for i in range(N):
        graph.append(list(map(int, input())))
"""

dfs(0, 0, Move)
