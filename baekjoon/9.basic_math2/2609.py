# 최대공약수와 최소공배수 구하기
# 유클리드 호제법 사용

import sys
input = sys.stdin.readline

def GCD(x, y): # 최대 공약수
    flag = True
    while(flag):
        if x % y == 0:
            return y
            # x를 y로 나눴을 때의 나머지 값이 0일 때의 y값이 최대 공약수
        x, y = y, x % y

def LCM(x, y): # 최소 공배수
    return x * y // GCD(x, y)
    # x * y를 최대 공약수로 나눈 값 == 최소 공배수
x, y = map(int, input().split())
print(GCD(x, y))
print(LCM(x, y))