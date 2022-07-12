import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
R = H/2

# W = width
# H = Height
# X, Y = width와 height의 시작지점(왼쪽 최하단)
# P = 선수 수
# R = 반지름
cnt = 0
for i in range(P):
    tx, ty = map(int, input().split())
    # 선수들의 좌표

    if pow(R, 2) >= pow(tx-X, 2) + pow(ty-(Y+R), 2):
        cnt += 1    # 왼쪽 원 안에 포함되거나
    elif pow(R, 2) >= pow(tx-(X+W), 2) + pow(ty-(Y+R), 2):
        cnt += 1    # 오른쪽 원 안에 포함되거나
    elif X <= tx and X+W >= tx and Y <= ty and Y+H >= ty:
        cnt += 1    # 사각형 안에 포함되면 cnt++
print(cnt)