import sys
input = sys.stdin.readline

def circle_into_dot(cx, tx, cy, ty):
    return pow((cx-tx), 2) + pow((cy-ty), 2)

TC = int(input().strip())
for _ in range(TC):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    num = int(input().strip())
    for i in range(num):
        cx, cy, r = map(int, input().split())
        if pow(r, 2) >= circle_into_dot(cx, x1, cy, y1) or pow(r, 2) >= circle_into_dot(cx, x2, cy, y2):
            if pow(r, 2) >= circle_into_dot(cx, x1, cy, y1) and pow(r, 2) >= circle_into_dot(cx, x2, cy, y2):
                pass
            else:
                cnt += 1
    print(cnt)