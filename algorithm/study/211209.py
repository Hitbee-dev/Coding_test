# 프림 알고리즘
# 최소비용 생성나무를 찾는 알고리즘

# 1. MST에 속한 정점(S)과 남아있는 정점(V-S)을 기억한다.
# 2. 두 집합 S, V-S를 잇는 간선들을 찾고
# 3. 그 중 가장 짧은 간선을 찾는다.
# 4. 찾은 간선을 MST에 추가하고(출력)
# 5. 간선에 연결된 두 정점 중 V-S에 속한 노드를  S로 옮긴다.

# 프림 알고리즘 수행시간 : O(nlongn)

def extractMin(Q, D):
    pass # 정점 집합 Q에서 D[x]가 최소인 x를 리턴

def prim(s):
    #... <- 앞 장의 초기화 코드
    while S != V:
        # 최소 비용 노드 u를 방문한다(MST에 포함시킴).
        # 힙으로 구현 가능
        u = extractMin(V-S, D)
        S.add(u)

    return sum(D.values())

V = set()
S = set()
D = {}
print('(prim) MST=', prim(1))
