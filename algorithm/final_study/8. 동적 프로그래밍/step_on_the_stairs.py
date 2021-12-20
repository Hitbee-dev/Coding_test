# 계단 밟기 문제
# • 계단을 1칸 또는 2칸을 오를수있다.

# • 입력
# – 계단마다 얻을 수 있는 점수가 있고, 계단을 밟으면 그 계단의 점수를 더한다.
# – 점수는 음수가 될 수도 있다. 계단의 개수 n과 계단의 점수들이 입력으로 주어진다.
# – S = {s1, s2, ..., sn}

# • 출력
# – 계단을 끝까지 올라서 얻을 수 있는 가장 많은 점수

# • 문제의 정의: M(S, k) (편의상 M(k)라고 하자)
# – k번째 계단까지 올라서 얻을 수 있는 가장 많은 점수

# • 풀이:k번째 계단을 오르는 방법은 두 가지
#     • (k-1)번째 계단에서 한 칸 오르기
#     • → (k-1)번째 계단까지 최대점수 + k번째 계단의 점수
#         M(k-1)
#     • (k-2)번째 계단에서 두 칸 오르기
#     • → (k-2)번째 계단까지 최대점수 + k번째 계단의 점수
#         M(k-2)

# – M(k) = s1 + max(M(k-1), M(k-2))
# – M(0) = 0, M(1) = s1

# 재귀적인 해법
def stair_rec(S, k):
    if k <= 1: # 만약 현재 계단이 1이나 0이면
        return S[k] # 현재 계단의 점수를 리턴한다.
    return S[k] + max(stair_rec(S, k-1), stair_rec(S, k-2))
    # 현재 계단의 위치 + (전 계단, 전전 계단 중 값이 큰 계단)

stairs_rec = [1, -6, 7, 3, -9, -3, 7, -4, -5, -2]
print(stair_rec(stairs_rec, len(stairs_rec)-1)) # 인덱스 값(계단의 위치)는 0부터 시작하기 때문에 -1

# Memoization
def stair_memo(S, k, dp):
    if k in dp: # 만약 전에 계산한 값이 있다면
        return dp[k] # 바로 리턴
    
    dp[k] = S[k] + max(stair_memo(S, k-1, dp), stair_memo(S, k-2, dp)) # dp에 기억
    return dp[k]

stairs_memo = [1, -6, 7, 3, -9, -3, 7, -4, -5, -2]
dp = [0 for _ in range(len(stairs_memo))] # 미리 0으로 채운 배열을 만들어 줌
dp[0] = stairs_memo[0] # dp[0]을 stairs[0]으로 초기화
dp[1] = stairs_memo[1] # dp[1]을 stairs[1]으로 초기화
print(stair_memo(stairs_memo, len(stairs_memo)-1, dp))

# Dynamic Programming
def stair_dp(S, k):
    dp[0] = S[0] # dp[0]을 stairs[0]으로 초기화
    dp[1] = S[1] # dp[1]을 stairs[1]으로 초기화
    for i in range(2, k+1): # 2부터 k까지 반복
        dp[i] = S[i] + max(dp[i-1], dp[i-2]) # dp[i]에 계단의 위치 + (전 계단, 전전 계단 중 값이 큰 계단)
    return dp[k] # 함수가 아닌 dp를 계산한 값을 리턴

stairs_dp = [1, -6, 7, 3, -9, -3, 7, -4, -5, -2]
dp = [0 for _ in range(len(stairs_dp))] # 미리 0으로 채운 배열을 만들어 줌
print(stair_dp(stairs_dp, len(stairs_dp)-1))
