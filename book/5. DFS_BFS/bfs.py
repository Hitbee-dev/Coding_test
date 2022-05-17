# BFS

from collections import deque

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 이용
    queue = deque([start])
    print(f"Queue: {queue}")
    # 현재 노드를 방문 처리
    visited[start] = True
    while queue:
        print(visited)
        # 큐에서 하나의 원소를 뽑아 출력하기
        print(f"원소 제거 전: {queue}")
        v = queue.popleft()
        print(f"원소 제거 후: {queue}")
        print(v, end=" ")
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        print("==========================")

# 각 노드가 연결된 정보를 표현
graph = [
    [],        # 0번 노드는 비워둠(index 그대로 사용하기 위해)
    [2, 3, 8], # 1번 노드에 연결되어있는 노드들
    [1, 7],    # 2번 노드에 연결되어있는 노드들
    [1, 4, 5], # 3번 노드에 연결되어있는 노드들
    [3, 5],    # 4번 노드에 연결되어있는 노드들
    [3, 4],    # 5번 노드에 연결되어있는 노드들
    [7],       # 6번 노드에 연결되어있는 노드들
    [2, 6, 8], # 7번 노드에 연결되어있는 노드들
    [1, 7]     # 8번 노드에 연결되어있는 노드들
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9

# 정의된 bfs 함수 호출
bfs(graph, 1, visited)