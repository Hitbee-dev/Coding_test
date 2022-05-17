# 꼬리 재귀는 스택을 쌓는 형식의 재귀가 아니기 때문에 메모리 사용량이 매우 적다.
# 따라서 함수 재사용이 가능하다.

# 일반적인 반복문 형태
def example(n):
    result = 0
    for i in range(n):
        result += i
    return result
print(example(1001))

# 일반적인 재귀 형태
def recur(n):
    if n == 1:
        return 1
    return n + recur(n-1)
print(recur(1000))

# 꼬리 재귀 형태
def tail_recur(n, m):
    if n == 0:
        return m    
    return tail_recur(n-1, n+m)
print(tail_recur(1000, 0))

"""
    하지만, 꼬리 재귀를 사용해도 Stack Overflow가 일어나는 것을 알 수 있다.
    이유로는, 컴파일러가 해주는 기능이기 때문에 Stack Overflow가 일어나는 것이다.
"""