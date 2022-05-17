# 균형탐색이진트리: 레드블랙트리의 특징
# 1. 모든 Node는 red/black 둘 중 하나의 색으로 되어있다.
# 2. root Node는 black이다.
# 3. Leaf(None) Node는 black이다.
# 4. red Node의 자식(Child)Node는 무조건 black이다.
# 5. root Node에서 Leaf Node로 가는 black Node의 개수가 항상 같아야 한다.

# h(v) = v의 높이(height)
# bh(v) = v가 Leaf Node까지 갈 경우의 높이(height)
    # v를 제외한 black Node의 개수
# NIL = None, Leaf Node라고 한다.

# 사실1: v의 서브트리의 내부 Node개수 >= 2^bh(v) - 1
# 증명: h(v)에 대한 귀납법
# BestCase: h(v) = 0 == Leaf Node가 1개밖에 없는 것