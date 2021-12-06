V = {0, 1, 2, 3, 4}
N = len(V)
E = {(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 4)}
G = (V, E)

adjMatrix = [[0] * N for _ in range(N)] # 2차원 배열 생성

for i in range(N):
    for j in range(N):
        if (i, j) in E:
            adjMatrix[i][j] = 1 # 인접행렬의 값을 1로 설정
            adjMatrix[j][i] = 1 # (0, 1)이나 (1, 0)이나 같기 때문에 이 좌표도 1로 설정

for row in adjMatrix:
    print(row)


adjList = {v: [] for v in V} # 인접리스트 생성

for x, y in E:
    adjList[x].append(y) # [] -> [y]
    adjList[y].append(x) # [] -> [x]
    print()
    for v in V:
        print(v, '->', adjList[v])

