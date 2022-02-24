# 부품 찾기

"""
    N개의 부품을 가지고있다.
    각 부품은 정수 형태의 고유한 번호가 있다.
    손님은 M개 종류의 부품을 대량으로 구매하려한다.
    가게안에 부품이 모두 있는지 확인하는 프로그램을 작성하라.
"""

# 입력 예시     | 출력 예시
# 5           | no yes yes
# 8 3 7 9 2
# 3
# 5 7 9

def python_search(na, ma):
    result = []
    for m in ma:
        if m in na:
            result.append("yes")
        else:
            result.append("no")
    return result

def binary_search(na, ma):
    na.sort()
    ma.sort()
    result = []
    for i in ma:
        buf = na
        check = 0
        while True:
            # print(f"길이: {len(buf)}, 값: {buf}")
            if len(buf) == 1:
                if i == buf[0]:
                    check = 1
                else:
                    check = 2
                break
            if i < buf[len(buf) // 2]:
                buf = buf[:len(buf) // 2]
            elif i > buf[len(buf) // 2]:
                buf = buf[len(buf) // 2:]
            else:
                check = 1
                break

        if check == 1:
            result.append("yes")
        else:
            result.append("no")
    return result

# N = 5
# N_Arr = [8, 3, 7, 9, 2]
# M = 3
# M_Arr = [5, 7, 9]

N = int(input())
N_Arr = list(map(int, input().split()))
M = int(input())
M_Arr = list(map(int, input().split()))

RESULT1 = python_search(N_Arr, M_Arr)
RESULT2 = binary_search(N_Arr, M_Arr)

print("파이썬 For Each문 활용으로 해결")
for i in range(M):
    print(RESULT1[i], end=" ")
    
# 이진 탐색 방법의 경우 sort를 하고 시작하기 때문에 yes와 no의 위치가 바뀔 수 있음
# 해결하려면 하겠는데 코드가 너무 길어지는데.. 이렇게 푸는게 맞나싶다
print("\n\n이진탐색으로 해결")
for i in range(M):
    print(RESULT2[i], end=" ")