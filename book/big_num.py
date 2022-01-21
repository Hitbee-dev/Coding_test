# 큰 수의 법칙

# N = 배열의 개수
# M = 반복할 횟수
# K = 한 원소당 반복 가능한 횟수

# 큰 수 순서대로 반복해서 최고의 합을 구하는 문제

N, M, K = map(int, input().split())
Array = list(map(int, input().split()))
Array.sort(reverse=True) # 큰 수 대로 정렬

def bignum(m, k, arr):
    cnt, result = 0, 0
    while cnt != m: # cnt가 반복할 횟수가 될 때 까지 반복
        for _ in range(k): # 배열의 가장 큰 것을 반복 가능한 횟수만큼 반복
            print(f"{result}+{arr[0]}")
            result += arr[0]
            cnt += 1
        print(f"{result}+{arr[1]}")
        result += arr[1] # 반복 가능한 횟수가 끝나면 두번째 큰 수를 한번 사이에 넣어준다.
        cnt += 1
    return result
            
print(bignum(M, K, Array))