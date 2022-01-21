# 1이 될 때 까지
""" 요약
    나누었을 때 나머지 값(나머지 값은 빼려는 횟수랑 같기 때문) + 
    나머지 값이 0이면 계속 나눠서 1이 될 때까지 반복한 횟수
"""

N, K = map(int, input().split())

def until(n, k):
    cnt = 0
    while n != 1:
        if n%k == 0:
            cnt += 1
            n = n//k
        else:
            cnt += n%k
            n = n-(n%k)
    return cnt
print(until(N, K))