# 상하좌우

# 여행가 A는 N x N크기의 정사각형 공간위에 서 있다.
# 이 공간은 1 x 1크기의 정사각형으로 나누어져 있으며,
# 가장 왼쪽 위 좌표는 (1, 1)이고 가장 오른쪽 아래 좌표는 (N, N)이다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다.
# 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여있다.

# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D중 하나의 문자가 반복적으로 적혀있다.
# 각 문자의 의미는 다음과 같다.

# L: 왼쪽으로 한칸 이동
# R: 오른쪽으로 한칸 이동
# U: 위로 한칸 이동
# D: 아래로 한칸 이동

# 이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
# 예를들어 (1, 1)의 위치에서 L 혹은 U를 만나게되면 무시된다.
# 계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.

""" 요약
    여행가가 이동해서 최종적으로 있는 위치를 출력해라.
    항상 여행가는 (1, 1)에서 시작한다.
    단, 움직일 수 없는경우 무시하고 다음 계획서로 진행하라.
"""

# 입력 예시      |   출력 예시
# 5             |    3 4
# R R R U D D

Size = int(input())
Array = list(map(str, input().split()))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이동 문자
move_types = ["U", "D", "L", "R"]

# 현재 위치
x, y = 1, 1

# 조건 검사
def func(n, s):
    global x, y, dx, dy
    if x+dx[n] >= 1 and y+dy[n] >= 1 and x+dx[n] <= s and y+dy[n] <= s:
        x += dx[n]
        y += dy[n]

def udlr(size, arr):
    for i in arr:
        for n, j in enumerate(move_types):
            if i == j:
                func(n, size)

udlr(Size, Array)
print(x, y)