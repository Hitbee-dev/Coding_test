# 떡볶이 떡 만들기

"""
    떡은 한번에 자른다.
    떡의 개수 N과, 필요한 떡의 길이 M이 첫번째 줄에 주어지고,
    각 떡의 길이가 두번째 줄에 주어진다.
    이 때 절단기에서 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
    적어도 M길이 만큼의 떡을 집에 가져가기 위해 절단기에서 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
"""

# 입력 조건     | 출력 조건
# 4 6         | 15
# 19 15 10 17

def tteok(n, m, arr):
    buffer = [x-min(arr) for x in arr]
    while True:
        # 제일 작은 값을 기준으로 잘랐는데 만약 원하는 길이보다 크다면
        if sum(buffer) > m:
            # 전부 길이 1씩 줄이기
            for i in range(n):
                # 근데 이미 0이라면 그대로 두기
                if buffer[i] == 0:
                    pass
                else:
                    buffer[i] -= 1
        # 원하는 길이와 같다면 반복문 종료
        elif sum(buffer) == m:
            break
        # 원하는 길이보다 작아졌다면
        else:
            # 전부 길이 1씩 늘리고 반복문 종료
            buffer[i] = [x+1 for x in range(n)]
            break
    return buffer

N, M = map(int, input().split())
Arr = list(map(int, input().split()))
print(max(Arr) - max(tteok(N, M, Arr)))
