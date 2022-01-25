# 유클리드 호재법

""" 요약
    A와 B의 나머지 값이 0이 될 때 까지 반복한다.
    나머지값이 0이될 때의 값이 A와 B의 최대공약수이다.
"""

A, B = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

print(gcd(A, B))

    