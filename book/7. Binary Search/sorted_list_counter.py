# 정렬된 배열에서 특정 수 갯수 세기

"""
    시간복잡도가 O(logN)을 넘으면 안되기 때문에 for는 사용할 수 없음
"""

# 입력 조건       | 출력 조건
# 7 2           | 4
# 1 1 2 2 2 2 3

from collections import Counter
from bisect import bisect_left, bisect_right

def count_by_range(arr, lv, rv):
    li = bisect_left(arr, lv) # 찾으려는 값을 왼쪽에서부터 찾음(인덱스로 반환)
    ri = bisect_right(arr, rv) # 찾으려는 값을 오른쪽에서부터 찾음(인덱스로 반환)
    return ri-li

N, M = map(int, input().split())
data = list(map(int, input().split()))

if Counter(data)[M] == 0 or count_by_range(data, M, M) == 0:
    # 만약 찾는 값이 없으면 -1 반환
    print(-1)
else:    
    # 참고로 카운터 라이브러리의 시간복잡도는 O(N)로, O(logN)보다 느리다.
    print(Counter(data)[M])
    # bisect 라이브러리의 시간복잡도는 O(logN)으로 조건에 만족한다.
    print(count_by_range(data, M, M))