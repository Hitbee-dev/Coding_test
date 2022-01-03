""" DP(Dynamic Programming)란?
    재귀적 호출에서 크기가 같은 문제에 대한 호출이 심하게 중복되는 문제를 해결하기 위해
    한번 풀이한 해의 Solution을 기억하여 중복호출을 제거하는 방법이다.
"""

# 1부터 n까지 더하는 함수
def sum_1_to_n(n):
    if n == 1:
        return 1
    return n + sum_1_to_n(n-1)
print(sum_1_to_n(1000))

# DP를 사용한 1부터 n까지 더하는 함수
def sum_1_to_n_dp(n):
    sol = [0 for _ in range(n+1)] # 0으로 된 1000개의 배열 생성
    sol[1] = 1  # 1부터 시작하므로 1번째 인덱스에 1을 넣어준다.

    for i in range(2, n+1):
        sol[i] = sol[i-1] + i # 인덱스가 2부터 시작하므로 i-1을 해준다.
    return sol[n]
print(sum_1_to_n_dp(1000))