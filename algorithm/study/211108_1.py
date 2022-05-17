#1부터 n까지 합하는 동적 프로그래밍
n = int(input())

def acc(n):
    if n == 1:
        return 1
    else:
        return n + acc(n-1)

def fib(n):
    global dp
    if n in dp:  # 기억해 둔 해가 있으면 사용
        return dp[n]

    dp[n] = fib(n-1) + fib(n-2)  # return하기 전에 새로 구한 해를 dp에 기억시킴
    return dp[n]

def acc_modify(n):
    global dp
    if n in dp:
        return dp[n]

    dp[n] = n+acc_modify(n-1)
    return dp[n]

dp = {1: 1, 2: 1}
print(f"전체 합: {acc(n)}") #전체 합
print(f"중복 제거된 결과: {fib(n)}") #중복 제거된 결과
print(f"중복 제거된 결과: {acc_modify(n)}") #중복 제거된 결과
