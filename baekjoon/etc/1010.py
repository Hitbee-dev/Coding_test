import sys

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    #경우의 수는 m! // (n!*(m-n)!)이다.
    bridge = factorial(m) // (factorial(n) * factorial(m-n))
    print(bridge)