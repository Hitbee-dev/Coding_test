def dfs(L, v, visited: set):
    for w in L[v] - visited:
        visited.add(w)
        dfs(L, w, visited)


def is_connected(V: set, E):
    L = {v: set() for v in V}
    for x, y in E: L[x].add(y); L[y].add(x)

    visited = set()
    s = list(V)[0]  # 임의의 시작 정점
    dfs(L, s, visited)
    return V == visited


V = {1, 2, 3, 4, 5}
E1 = {(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 5), (4, 5)}
E2 = {(1, 2), (1, 3),(2, 3), (2, 5), (3, 5)}
print(is_connected(V, E1))  # --> True
print(is_connected(V, E2))  # --> False


def dijkstra(V, E, L, s):
    D = {v: WEIGHT_MAX for v in V}; D[s] = 0
    S = set()
    while S != V:
        u = min(V - S, key=lambda x: D[x])
        S.add(u)
        for v in L[u] - S:
            D[v] = min(D[v], D[u] + E[(u, v)])

    return D


WEIGHT_MAX = 1000
V = {1, 2, 3, 4, 5}
E = {(1, 2):3, (1, 3):4, (1, 4):3, (2, 3):2, (2, 5):6, (3, 5):2, (4, 5):7}
L = {v:set() for v in V}
for x, y in E: L[x].add(y)
print(dijkstra(V, E, L, 1))  # --> {1: 0, 2: 3, 3: 4, 4: 3, 5: 6}


from heapq import *

def heapsort(heap):
    heapify(heap)  # 배열을 힙 구조로 만든다(minheap).
    print(heap)  # <-- 여기
    while heap:
        print(heappop(heap), end=' ')

heapsort([83, 77, 23, 11, 96])
print()


def bluemarble(size):
    dp = [1] + [0] * size
    for n in range(1, size + 1):
        for dice in [1, 2, 3, 4, 5, 6]:
            k = n - dice
            if k < 0: break
            dp[n] += dp[k]

    return dp[size]


print(bluemarble(10))


def sum_(n, m):
    ret_val = 0
    for i in range(n, m + 1):
        ret_val += i

    return ret_val


def rsum(n, m):
    if n > m:
        return 0
    else:
        # return (A) + rsum(___(B)___, m)
        return n + rsum(n + 1, m)


print(sum_(1, 100))
print(rsum(1, 100))