# DFS

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    print(visited)

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        print(f"{i}의 방문 여부를 알아보겠습니다.")
        # 방문하지 않은 곳이라면
        if not visited[i]:
            print("================================")
            print()
            dfs(graph, i, visited)
        # 모두 방문했다면 for문 탈출
        elif visited.count(False) == 1:
            print("모두 방문하였습니다.")
            break
        else:
            print(f"방문했던 곳이므로 {i}를 나오겠습니다.")
        

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

# 정의된 dfs 함수 호출
dfs(graph, 1, visited)