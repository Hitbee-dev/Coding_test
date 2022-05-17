# Memoization은 한번 구한 해를 기억하여 중복 호출을 제거하는 방법이다.

# 피보나치 수열 재귀
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)
print(fibo(10))

# 피보나치 수열 Memoization
def fibo_memo(n):
    global dp
    if n in dp: # 기억해둔 해가 있다면 사용
        return dp[n]
    dp[n] = fibo_memo(n-2) + fibo_memo(n-1) # return 하기 전에 새로 구한 해를 기억해둔다.
    return dp[n]

dp = {1:1, 2:1} # sub-optimal solution을 기억 할 자료구조
print(fibo_memo(10))