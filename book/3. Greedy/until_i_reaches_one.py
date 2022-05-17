# 1이 될 때 까지
""" 요약
    나누었을 때 나머지 값(나머지 값은 빼려는 횟수랑 같기 때문) + 
    나머지 값이 0이면 계속 나눠서 1이 될 때까지 반복한 횟수
"""

N, K = map(int, input().split())

def until(n, k):
    cnt = 0
    while n != 1: # n이 1이 될 때 까지 반복
        if n%k == 0:
            cnt += 1
            n = n//k
        elif n < k: # 한번에 빼버려서 n이 k보다 작아졌을 때
            cnt += k-n
            n = k-n
        else:
            cnt += n%k
            n = n-(n%k)
    return cnt
print(until(N, K))