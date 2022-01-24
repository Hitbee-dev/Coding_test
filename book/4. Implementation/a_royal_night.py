# 왕실의 나이트

""" 요약
    체스판은 8 x 8이다.
    나이트는 말을 타고있기 때문에 L자 형태로만 이동할 수 있으며, 정원밖으로는 나갈 수 없다.
    수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동할 수 있으며,
    수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동할 수 있다.
    행 위치는 1~8, 열 위치는 a~h로 표현한다.
"""

move_types = input()

def a_royal_night(move):
    cnt = 0

    # 체스 판의 행렬
    columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
    rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

    # 현재 위치
    x, y = 0, 0

    # 움직일 수 있는 경우의 수
    dx = [2, 2, -2, -2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, 2, 2, -2, -2]

    for i in range(len(dx)):
        if columns.index(move[0]) - dx[i] > -1 and columns.index(move[0]) - dx[i] < 8 and rows.index(move[1]) - dy[i] > -1 and rows.index(move[1]) - dy[i] < 8:
            cnt += 1
    return cnt

print(a_royal_night(move_types))