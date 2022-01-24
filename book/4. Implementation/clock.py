# 시각

""" 요약
    00시 00분 00초 ~ N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
"""

N = int(input())

hour, min, sec = 0, 0, 0

def clock(n, h, m, s):
    cnt = 0
    while True:
        if n == h-1 and m == 0 and s == 0:
            break
        if "3" in str(h) or "3" in str(m) or "3" in str(s):
            cnt += 1
        s += 1 # 초 
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1

    return cnt

print(clock(N, hour, min, sec))