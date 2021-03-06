# 피보나치 수열을 반복문으로 바꿔보자.
# 이걸 할 줄 알아야 꼬리 재귀를 이해할 수 있다.

# 피보나치 수열 재귀 함수
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)
print(fibo(10))

# 피보나치 수열 반복문
def fibo_for(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        t = b
        b = a + b
        a = t
        print(a)
    return b
print(fibo_for(10))

# 피보나치 수열 꼬리 재귀 함수
def helper(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    return helper(n-1, b, a+b)

def tail_fibo(n):
    return helper(n, 0, 1)
print(tail_fibo(10))
    
"""
    C, C++ = Tail Call Optimization을 컴파일러에서 제공함
    Java, Python = Java는 메모리 모델, Python은 스택 트레이스등의 이유로 제공되지 않음
        단, 이진 탐색 알고리즘(Binary Search Algorithm)에는 사용할 수 있다.
    Lisp, Haskel = 순수 함수형 프로그래밍 언어에는 반복문 자체가 없기 때문에 꼬리재귀 형태가 필수로 사용됨
"""

""" 재귀적 해법의 바람직한 예
    1. 퀵정렬, 병합정렬등의 정렬 알고리즘
    2. 계승(factorial)구하기
    3. 그래프의 DFS
"""

""" 엄청난 중복이 발생되는 예(바람직하지 않은 예)
    1. 피보나치 수열
    2. 행렬곱셈 최적순서 구하기
"""