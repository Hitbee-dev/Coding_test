def bfs(v):
    Q = [v]
    while Q:
        v = Q.pop(0)
        print(v)

        for w in L(v):
            if w not in visited:
                visited.add(w)
                Q.append(w)

visited = set()
bfs(0)