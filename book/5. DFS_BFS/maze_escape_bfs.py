# 미로탈출 BFS

""" 요약
    DFS/BFS중 왜 BFS를 사용했냐면,
    BFS를 이용해서 너비를 우선탐색하게되면
    여러 갈래로 갈리는 경로 중에서 가장 짧게 갈 수 있는 경로를 알 수 있기 때문이다.
"""

from collections import deque

def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 사용
    queue = deque()
    # 튜플로 x, y의 값을 queue에 삽입
    queue.append((x, y))
    # queue가 빌 때 까지 반복
    while queue:
        print("==================================================")
        print(f"Before: {x}, {y}, {queue}")
        x, y = queue.popleft()
        print(f"After: {x}, {y}, {queue}")
        for i in graph:
            print(i)
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드(현재 위치)를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                # 첫 방문 위치는 무시
                if nx == 0 and ny == 0:
                    continue
                print(f"현재 위치({nx}, {ny})를 {graph[x][y] + 1}로 바꾸겠습니다.")
                graph[nx][ny] = graph[x][y] + 1
                print(f"{queue}에 {(nx, ny)}를 삽입하겠습니다.")
                queue.append((nx, ny))
    return graph[N-1][M-1]

graph = [
    [1, 1, 1, 1, 1, 1], 
    [0, 1, 0, 0, 0, 0], 
    [1, 1, 0, 1, 1, 1], 
    [1, 0, 0, 1, 0, 1], 
    [1, 1, 1, 1, 0, 1]
]
N, M = 5, 6
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0, 0))